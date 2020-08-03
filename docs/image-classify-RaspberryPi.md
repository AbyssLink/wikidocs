# 一个基于树莓派的元器件识别工具

## 概述

基于 Node-RED 实现的一个元器件识别工具，提供 UI 界面控制预测与训练元器件图像。

## 硬件

树莓派 + USB 摄像头， 主机，无线路由器

## 软件

![](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/2018-12-18_02-55.png)

Node-RED UI 作为用户界面，可控制拍摄图像，对拍摄的图像进行预测，或开始自定义的训练。

Node-RED 后台中自定义训练和预测两个节点，这两个节点通过调用 Python 脚本完成图像的识别或训练。

Python 脚本基于 imageAI 这个 Python 库实现，该库封装了打标和模型预设等操作，留下选取模型，训练次数，批次大小，是否优化输出等参数供用户选择，简化了训练和预测的流程。

## 工作流程

1.  树莓派负责图像的拍摄和传输，因该模型的算法比较耗时，预测、训练、结果显示等操作在主机端进行。

2.  主机端可控制树莓派拍摄图像，并将生成的图像存储为文件，通过 tcp 协议，以 buffer 的形式发送到主机端并保存本地。

3.  主机调用特定已训练好的模型，生成识别的结果。

![take photo](https://github.com/AbyssLink/pic/blob/master/custom/2018-12-18_02-56.png?raw=true)

4. 主机可获取用户自定义的模型参数，训练生成模型。

![2018-12-18_02-56_1](https://github.com/AbyssLink/pic/blob/master/custom/2018-12-18_02-56_1.png?raw=true)

5. 上述流程的 Node-RED 流程如下。

![](https://github.com/AbyssLink/pic/blob/master/custom/2018-12-18_13-02.png?raw=true)

## 具体实现

#### 1. 从 NodeJS 调用 Python 函数：

Node-RED 是一个 Nodejs 应用程序，可以使用 Node 预制的 `child_process`模块。该模块提供了衍生子进程的功能，并可直接调用 shell 脚本，相当于执行了整个 Python 文件。示例:

```javascript
var spawn = require("child_process").spawn;
var process = spawn('python',["path/to/script.py", arg1, arg2, ...]);
```

Node 主线程中监听 Python 的数据：

```javascript
process.stdout.on("data", function (data) {
  //...
});
```

为了方便传送给 Python 的参数方便解析，传入 Json 或 对象，并分别解析：

```javascript
function (msg, out, err) {
    msg = msg.payload || '';
    if (typeof msg === 'object') {
        msg = JSON.stringify(msg);
    } else if (typeof msg !== 'string') {
        msg = msg.toString();
    }
```

#### 2. 为 Python 脚本指定不同的模型进行训练

基于 keras 实现， keras 的封装使得 tensorflow 的使用变得更加简明易懂，具体调用如下：

SqueezeNet, 定义一个通用结构，基于 imageNet 预训练的权重：

```python
def SqueezeNet(include_top = True, weights="imagenet", model_input=None, non_top_pooling=None, num_classes=1000, model_path = ""):

    if(weights == "imagenet" and num_classes != 1000):
        raise ValueError("You must parse in SqueezeNet model trained on the 1000 class ImageNet")

    image_input = model_input

    network = Conv2D(64, (3,3), strides=(2,2), padding="valid")(image_input)
    network = Activation("relu")(network)
    network = MaxPool2D( pool_size=(3,3) , strides=(2,2))(network)
    ...
```

ResNet, 定义一个通用结构，基于 imageNet 预训练的权重：

```python
def ResNet50(include_top=True, non_top_pooling=None, model_input=None, num_classes=1000, weights='imagenet', model_path=""):
    layers = [3,4,6,3]
    channel_depths = [256, 512, 1024, 2048]

    input_object = model_input

    output = Conv2D(64, kernel_size=7, strides=2, padding="same")(input_object)
    output = BatchNormalization()(output)
    output = Activation("relu")(output)

    output = MaxPool2D(pool_size=(3,3), strides=(2,2))(output)
    output = resnet_first_block_first_module(output, channel_depths[0])
    ...
```

InceptionV3, 定义一个通用结构，基于 imageNet 预训练的权重：

```python
def InceptionV3(include_top=True,
                weights='imagenet',
                input_tensor=None,
                model_input=None,
                pooling=None,
                classes=1000, model_path=""):

    img_input = model_input
    channel_axis = 3

    x = conv2d_bn(img_input, 32, 3, 3, strides=(2, 2), padding='valid')
    x = conv2d_bn(x, 32, 3, 3, padding='valid')
    x = conv2d_bn(x, 64, 3, 3)
    x = MaxPooling2D((3, 3), strides=(2, 2))(x)
    ...
```

Densenet，可调用 Keras 的模型生成结构：

```python
# API entries importable from `keras.models`:
Model = training.Model

inputs = img_input
# Create model.
model = Model(inputs, x, name='densenet')
```

#### 3. 基于 Node-RED 实现树莓派与主机间通信

使用 tcp 节点实现树莓派与主机间通信，传送图片与字符串。基于 socket 创建一个连接，发送端使用 python 的 struct 库将比特串打包，再在接收端解包，如：

```python
// Sender:
size = bin(size)[2:].zfill(16) # encode filename size as 16 bit binary
// Reciver:
size = clientsocket.recv(16)
```

#### 4.模型的训练

本次实验作为原型，未收集照片，转而从网络获取，共 3 类，为常见元器件中的 nodemcu, ssd1306 与 DHT11，共 100 张左右图像。

使用 ResNet 以 16 张图片为一个批次训练 10 个 Epoch 后，测试集上模型准确率在 82.5% 左右。但实际上在现实中的使用识别准确率并不高，主要是预测环境与数据集的图片拍摄的环境相差过大导致的。后期数据集需要与预测环境相匹配，并扩大数据集以提升准确率。

## TO-DO:

1. Node-RED UI 中实现动态刷新图片。
2. UI 中自定义 html，显示出拍摄好的图片与训练好的模型，供用户进行选择。
3. 优化树莓派与主机通信方式，改 tcp 为 http 通信。

## 项目依赖

**JavaScript** : Nodejs >6.1.1, Node-RED==0.19.5

**Python**: Imageai, Tensorflow 1.4.0+ , SciPy 0.19.1+, Numpy 1.13.1+,

OpenCV, pillow , Matplotlib , h5py, Keras 2.x

## 使用方法

download the repositories:

```shell
git clone https://github.com/AbyssLink/Node-RED-new-node.git
cd Node-RED-new-node
```

Install on Mac OS or Linux:

```shell
cd ~/.node-red
npm install ~/<PATH-TO-YOUR-DIRECTORY>/imageai-training
npm install ~/<PATH-TO-YOUR-DIRECTORY>/imageai-predict
```

Install on Windows:

```powershell
cd C:\Users\my_name\.node_red
npm install C:\<PATH-TO-YOUR-DIRECTORY>\imageai-training
npm install C:\<PATH-TO-YOUR-DIRECTORY>\imageai-predict
```
