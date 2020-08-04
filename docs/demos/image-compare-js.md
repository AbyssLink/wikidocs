# 图片相似度 JS 库

## Code

https://github.com/AbyssLink/image-hash-js

## 图像数据结构

矩阵（Matrix）是用于图像的低级表示的最常见的数据结构。本库中所处理的数字图像是一个具有整数像素数据的多维矩阵，由 CCD 摄像头输出。

## 基于哈希算法的图像分类

模版匹配是一种最原始和基本的模式识别方法，研究某一特定对象物的图案位于图像的什么地方，进而识别对象物，是图像处理中最基本且常用的匹配方法。由于传送带的摄像头到传送带的位置是固定不变的，可以认为每次获取的待分类对象物在图像中的位置是固定的，通过拍摄物体在相同位置的的图像作为模版，从而省去在大图像中搜寻目标模版的操作，将模版匹配问题转换为更简单的基于相似度匹配的问题。
该方法具有自身的局限性，若原图像中的匹配目标发生旋转或大小变化，该方法失效。

### 感知哈希介绍

使用感知哈希（Perceptual hash）算法可以提取图片的特征，为每张图片生成一个以 16 进制表示的特定长度的哈希值字符串，比较不同图片之间的哈希值字符串，两个哈希值字符串之间越相似即说明两张图片越相似。简要的实现流程如下所述：

1. 图像预处理：根据特征点的定位旋转图像为正向，将原始图像规格化为预设大小
2. 计算哈希值：计算图像的哈希值
3. 比较两张图片的相似度：计算两个哈希值的汉明距离
4. 设置阈值：设置特定的阈值作出判断，如认为汉明距离小于 5 的图片非常相似，大于 10 的图片则认为不相似。

### 图像预处理

以分类交通标志为例，为摄像机捕获原图的示例如下：

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/001.jpeg" height="180px" alt="图片说明" >
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/002.jpeg" height="180px" alt="图片说明" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/003.jpeg" height="180px" alt="图片说明" >
</div>
对图片进行规格化处理，缩小到特定的尺寸 $N * N$。以 $N = 8$ 为例，规格化后的图片包含 64 个像素：

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/001_resize.jpg" height="180px" alt="图片说明" >
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/002_resize.jpg" height="180px" alt="图片说明" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/003_resize.jpg" height="180px" alt="图片说明" >
</div>
将图片转为64级灰度。灰度转换的公式使用 PAL 和 NTSC 标准使用的 rec601 亮度（Y）分量计算标准：

$$
Y = 0.299R + 0.587G + 0.114B
$$

这样将数字图片从一个多维度二维矩阵转换为了单维二维矩阵：

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/001_gray.jpeg" height="180px" alt="图片说明" >
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/002_gray.jpeg" height="180px" alt="图片说明" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/003_gray.jpeg" height="180px" alt="图片说明" >
</div>

对图片进行缩放和灰度化处理的作用是去除图片的细节，只保留结构、明暗、轮廓等基本信息，防止因为不同尺寸和比例带来的图片差异。

注：由于哈希算法不具有旋转不变性，若物体非正向摆放，需要先识别出圆的边缘来识别出圆心，并根据识别出的特征点（绿点）位置求得夹角度数，从而将非正向摆放的标志旋转为正向，提高后续程序识别的准确性。具体操作由 实验室编译得到的 opencv.js 实现。

**JavaScript 实现**

```javascript
const imagePreProcess = async (imgPath) => {
  const resizeImgPath = await resizeImage(imgPath, 8, 8);
  let pixels = await retrivePixels(resizeImgPath);
  const row = pixels.shape[0];
  const col = pixels.shape[1];
  // console.log(row, col);
  // new array to store image info
  let arr = create2DArray(row);
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      const r = pixels.get(i, j, 0);
      const g = pixels.get(i, j, 1);
      const b = pixels.get(i, j, 2);
      arr[i][j] = Math.round(0.299 * r + 0.578 * g + 0.114 * b);
    }
  }
  // console.log(arr);
  return arr;
};
```

注：基于感知哈希的实现里，上述代码使用了该实现所依赖的两个库（1. 获取图片像素；2. 图片尺寸压缩），这两个库后期可考虑使用原生 JavaScript 代替，使得该实现完全由原生 JavaScript 实现。

```json
"dependencies": {
    "get-pixels": "^3.3.2",
    "sharp": "^0.25.3"
}
```

### 平均哈希

1. 压缩图像为特定的尺寸 $N * N$，$N$ 是最终生成的哈希字符串的长度。
2. 累加图像的像素的值，计算图像的平均像素值为 $A$
3. 遍历图像的每一个像素 $P$，将像素归一化为二进制形式，获取哈希值为：

$$
h(i) = \left\{\begin{aligned}
0, P_i < A \\
1, P_i \geqslant A
\end{aligned}\right.
$$

简要的说，获取图片的平均哈希值，从每一行开始，从左到右检查像素，如果当前像素值 > 平均哈希值，哈希字串加 1，否则加 0。

**测试样例**

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/001.jpeg" height="180px" alt="图片说明" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/ahash.jpg" height="180px" alt="图片说明" >
</div>
**JavaScript 实现**

```javascript
const AHash = async (imgPath) => {
  let arr = await convertGrayscale(imgPath);
  let average = 0,
    sum = 0;
  let difference = "";
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      sum += arr[i][j];
    }
  }
  average = Math.round(sum / (arr.length * arr[0].length));
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      if (arr[i][j] > average) {
        difference += "1";
      } else {
        difference += "0";
      }
    }
  }
  hexadecimal = parseInt(difference, 2).toString(16);
  console.log("average hash = ", hexadecimal);
  return hexadecimal;
};
```

### 中位哈希

1. 压缩图像为特定的尺寸 $N * N$，$N$ 是最终生成的哈希字符串的长度。
2. 遍历图像的每一个像素$P$， 计算图像的中位像素值为 $M = median(P_i) \qquad (i=1,2,...N^2)$
3. 遍历图像的每一个像素 $P$，将像素归一化为二进制形式，获取哈希值为：

$$
h(i) = \left\{\begin{aligned}0, P_i < M \\1, P_i \geqslant M\end{aligned}\right.
$$

中位哈希和平均哈希很类似，只是把归一化的条件从平均值改为了中位数。

**测试样例**

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/001.jpeg" height="180px" alt="图片说明" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/mhash.jpg" height="180px" alt="图片说明" >
</div>
**JavaScript 实现**

```javascript
const MHash = async (imgPath) => {
  let arr = await convertGrayscale(imgPath);
  const median = getMedian(arr);
  let difference = "";
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      if (arr[i][j] > median) {
        difference += "1";
      } else {
        difference += "0";
      }
    }
  }
  hexadecimal = parseInt(difference, 2).toString(16);
  console.log("median hash = ", hexadecimal);
  return hexadecimal;
};
```

### 差异哈希

1. 压缩图像为特定的尺寸 $N * N$，$N$ 是最终生成的哈希字符串的长度。
2. 遍历图像的每一个像素 $P$，将像素归一化为二进制形式，获取哈希值为：

$$
h(i) = \left\{\begin{aligned}
0, P_i < P_{i+1} \\
1, P_i \geqslant P_{i+1}
\end{aligned}\right.
$$

简要的说，获取图片的差异哈希值，从每一行开始，从左到右检查像素，如果左像素值 > 右像素值（若左像素为行末则与下一行的起始像素比较），哈希字串加 1，否则加 0。

**测试样例**

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/001.jpeg" height="180px" alt="图片说明" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/dhash.jpg" height="180px" alt="图片说明" >
</div>
**JavaScript 实现**

```javascript
const DHash = async (imgPath) => {
  let arr = await convertGrayscale(imgPath);
  let difference = "";
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[0].length; j++) {
      if (arr[i][j] > arr[i][j + 1]) {
        difference += "1";
      } else {
        difference += "0";
      }
    }
  }
  hexadecimal = parseInt(difference, 2).toString(16);
  console.log("difference hash = ", hexadecimal);
  return hexadecimal;
};
```

### 块哈希

1. 将规格化后的图像分为非重叠的块 $I_1, I_2, ..., I_N$，$N$ 是最终生成的哈希字符串的长度。
2. 从相应的块序列 $ I_1,I_2,...,I_N$ 计算平均值序列 $M_1,M_2,...M_N$，并得到此序列的中位数为：

$$
M_d =  median(M_i)\qquad(i=1,2,...N)
$$

3. 将平均值序列归一化为二进制形式，并获得哈希值 h 为：

$$
h(i) = \left\{\begin{aligned}
0, M_i < M_d \\
1, M_i \geqslant M_d
\end{aligned}\right.
$$

简要的说，块哈希算法将图像划分为多个块，如果块内的均值大于等于中位数, 输出 1，小于则输出 0，这样为每个块生成一个值 1 或 0，这些值从左到右依次组合成一个哈希。

**测试样例**

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/001.jpeg" height="180px" alt="原始图像" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/bhash.jpg" height="180px" alt="哈希结果" >
</div>
**JavaScript 实现**

```javascript
const BHash = async (imgPath, bits = 8) => {
  let pixels = await retrivePixels(imgPath);
  const width = pixels.shape[0];
  const height = pixels.shape[1];
  blocksizeX = Math.ceil(width / bits);
  blockSizeY = Math.ceil(height / bits);

  result = [];

  for (let y = 0; y < bits; y++) {
    for (let x = 0; x < bits; x++) {
      value = 0;
      for (let iy = 0; iy < blockSizeY; iy++) {
        for (let ix = 0; ix < blocksizeX; ix++) {
          const cx = x * blocksizeX + ix;
          const cy = y * blockSizeY + iy;
          value += totalValueRGB(pixels, cx, cy);
        }
      }
      result.push(value);
    }
  }
  const blocksArr = blocksToBits(result, blockSizeY * blocksizeX);
  return bitsToHexHash(blocksArr);
};
```

### 汉明距离

在信息论中，两个等长字符串之间的汉明距离（Hamming distance）是两个字符串对应位置的不同字符的个数，即将一个字符串变换成另外一个字符串所需要替换的字符个数。
哈希字符串以 16 进制表示，因此在计算两个哈希字符串的距离时只需将其转换为 2 进制后进行异或运算即能得到汉明距离。

**Javascript 实现**

```javascript
const hammingDistance = (hash1, hash2) => {
  const difference =
    parseInt(hash1, 16).toString(10) ^ parseInt(hash2, 16).toString(10);
  binary = parseInt(difference, 10).toString(2);
  distance = 0;
  for (let i = 0; i < binary.length; i++) {
    if (binary[i] == "1") {
      distance += 1;
    }
  }
  return distance;
};
```

### 分类测试

左图为示例输入，右三图为模版：

<div align="center">
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/out.jpg" height="180px" alt="图片说明" >
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/001.jpeg" height="180px" alt="图片说明" >
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/002.jpeg" height="180px" alt="图片说明" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/org/003.jpeg" height="180px" alt="图片说明" >
</div>

对输入图像与模版分别求汉明距离，结果为：

| 类别     | 模版 1(机动车道) | 模版 2(左转) | 模版 3(禁止临时停放) |
| -------- | ---------------- | ------------ | -------------------- |
| 平均哈希 | 10               | 8            | 4                    |
| 中位哈希 | 10               | 7            | 2                    |
| 差异哈希 | 7                | 9            | 2                    |
| 块哈希   | 5                | 6            | 3                    |

定义阈值 <5 即为非常相似，故模版 3 匹配，输入图像分类为模版三的类别。

### 稳健性测试

在原图发生特定变换后是否仍能够保留其特征是衡量算法稳健性的重要标准。用于测试的图像变换方法包括：

- 高斯模糊
- 灰度化
- 增加亮度，降低亮度
- 增加对比度，降低对比度

示例变换，从左到右的图像分别为：原图，高斯模糊，增加亮度，降低亮度，增加对比度，降低对比度，灰度化。

<div align="center">
	<img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/transfer/723.jpeg" height="135px" alt="原始图像" >
    <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/transfer/smooth.jpeg" height="135px" alt="高斯模糊" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/transfer/add_brightness.jpeg" height="135px" alt="增加亮度" >
    <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/transfer/decrease_brightness.jpeg" height="135px" alt="降低亮度" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/transfer/add_contrast.jpeg" height="135px" alt="增加对比度" >
   <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/transfer/decrease_contrast.jpeg" height="135px" alt="降低对比度" >
  <img src="https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/transfer/gray.jpeg" height="135px" alt="灰度化" >
</div>

使用 Python 的 Pillow, OpenCV, skimage 库，对 100 张 COCO 通用数据集中的图像进行上述变换：

![Xnip2020-06-08_20-45-12](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/tmp/diff-image-dataset.jpg)

针对以上哈希算法，计算与原图的相似度，对汉明距离求和的结果为下：

| 变换类型     | 平均哈希(bit) | 中位哈希(bit) | 差异哈希(bit) | 块哈希(bit) |
| ------------ | ------------- | ------------- | ------------- | ----------- |
| 高斯模糊     | 96            | 237           | 152           | 35          |
| 增加亮度     | 421           | 878           | 622           | 541         |
| 降低亮度     | 257           | 628           | 387           | 374         |
| 增加对比度   | 190           | 597           | 409           | 272         |
| 降低对比度   | 346           | 713           | 620           | 378         |
| 灰度化       | 89            | 226           | 93            | 141         |
| 总和         | 1399          | 3279          | 2283          | 1741        |
| 总和(百分比) | 3.64%         | 8.54%         | 5.94%         | 4.53%       |

总结：

平均哈希在各种变换类型下的综合表现下很好，而中位哈希的表现相对误差较大。在上述算法中，块哈希在实际系统运行时表现最佳。

### 速度测试

针对以上哈希算法，对 100 张 COCO 通用数据集中的图像测试的结果：

| 变换类型   | 平均哈希(ms) | 中位哈希(ms) | 差异哈希(ms) | 块哈希(ms) |
| ---------- | ------------ | ------------ | ------------ | ---------- |
| 高斯模糊   | 2017         | 2037         | 2037         | 7800       |
| 增加亮度   | 2068         | 1868         | 1934         | 9506       |
| 降低亮度   | 1920         | 1945         | 2044         | 9115       |
| 增加对比度 | 1834         | 1912         | 1885         | 8617       |
| 降低对比度 | 1887         | 1850         | 1933         | 7445       |
| 灰度化     | 1925         | 2072         | 1949         | 8197       |
| 总和       | 11651        | 11684        | 11782        | 50680      |
| 总和(秒)   | 11.7         | 11.7         | 11.8         | 50.7       |

总结：

平均哈希、中位哈希和差异哈希的速度表现近似，而块哈希的运行速度相对明显较慢，可能的原因是为保证块大小和哈希字符串的拓展，计算哈希值前的图片缩放比例不足，造成相对其他的哈希方法计算量较大。计算识别时间的均值，在上位机上每一张图片的识别时间约在 0.11 ~ 0.51 秒。

## 基于颜色直方图

在图像处理和摄影中，颜色直方图（color histogram）表示图像中颜色的分布。 对于数字图像，颜色直方图表示在固定的颜色范围列表中每个颜色范围内具有颜色的像素数量，这些颜色范围跨越图像的颜色空间，即所有可能颜色的集合。

### 提取图片特征值

1. 对颜色区间进行简化，将像素值 $v$ 分成四个区：

| area 1            | area 2               | area 3                | area 4                |
| ----------------- | -------------------- | --------------------- | --------------------- |
| $0\leq v \leq 63$ | $64 \leq v \leq 127$ | $128 \leq v \leq 191$ | $192 \leq v \leq 255$ |

2. 红绿蓝三色共有 4 个区，形成 64 种组合， 统计每一种中包含的像素数量：

| R   | G   | B   | Pixel quantity |
| --- | --- | --- | -------------- |
| 0   | 0   | 0   | 32744          |
| 0   | 0   | 1   | 349            |
| 0   | 0   | 2   | 14             |
| 0   | 0   | 3   | 0              |
| 0   | 1   | 0   | 2              |
| 0   | 1   | 1   | 234            |
| 0   | 1   | 2   | 365            |
| 0   | 1   | 3   | 184657         |
| 0   | 2   | 0   | 0              |
| 0   | 2   | 1   | 0              |
| 0   | 2   | 2   | 17             |
| 0   | 2   | 3   | 663            |
| 0   | 3   | 0   | 0              |
| 0   | 3   | 1   | 0              |
| 0   | 3   | 2   | 0              |
| 0   | 3   | 3   | 0              |
| 1   | 0   | 0   | 16078          |
| ... | ... | ... | ...            |
| 3   | 3   | 3   | 1810           |

3. 将表中最后一栏的像素数量提取出来，形成一个 64 维向量，以该向量作为该图片的特征值。

   如：$vector = (32744, 349, 14, 0, 2, ...1810)$

**Javascript 实现**

```javascript
/**
 * convert image to a 64-dimensional vector
 * 将图像转换为 64 维向量
 *
 * @param {string} imgPath
 * @returns {object}
 */
const colorVector = async (imgPath) => {
  let pixels = await retrivePixels(imgPath);
  const width = pixels.shape[0];
  const height = pixels.shape[1];
  let vectors = Array(64).fill(0);
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      const r = getPartition(pixels.get(x, y, 0));
      const g = getPartition(pixels.get(x, y, 1));
      const b = getPartition(pixels.get(x, y, 2));
      const index =
        r * Math.pow(4, 2) + g * Math.pow(4, 1) + b * Math.pow(4, 0);
      vectors[index] += 1;
    }
  }
  return vectors;
};
```

### 计算图片相似度

提取图片的特征值后，求图片间的相似度即转换为求图片的两个特征向量 $A$，$B$ 之间的相似度。
使用欧几里得点积公式推导：

$$
similarity = cos(\theta) = \frac{A \cdot B}{\|A \| \|B \|} = \frac{\sum_{i=1}^n A_i \times B_i}{\sqrt{\sum_{i=1}^n (A_i)^2} \times \sqrt{\sum_{i=1}^n (B_i)^2}}
$$

**Javascript 实现**

```javascript
/**
 * calculate the cosine similiarity of two images based on color histogram
 * 基于颜色直方图计算两个图像的余弦相似度
 *
 * @param {string} firstImg
 * @param {string} secondImg
 * @returns {number}
 */
const colorSimiliarity = async (firstImg, secondImg) => {
  let vector1 = await colorVector(firstImg);
  let vector2 = await colorVector(secondImg);
  // calculate cosine similiarity of two vectors
  let dividend = 0,
    divisor = 1;
  for (let i = 0; i < vector1.length; i++) {
    dividend += vector1[i] * vector2[i];
  }
  let absVector1 = 0,
    absVector2 = 0;
  for (let i = 0; i < vector1.length; i++) {
    absVector1 += Math.pow(vector1[i], 2);
    absVector2 += Math.pow(vector2[i], 2);
  }
  absVector1 = Math.pow(absVector1, 0.5);
  absVector2 = Math.pow(absVector2, 0.5);
  divisor = absVector1 * absVector2;
  similarity = dividend / divisor;
  return similarity;
};
```

## 基于神经网络

基于 TensorFlow.js，使用卷积神经网络（CNN）进行分类。主要流程如下：

1. 进行图像预处理，由于 CNN 不具有旋转不变性需要将非正向的图像转为正向。
2. 建立待训练的模型（CNN）
3. 卷积（Convolution）向图像应用滤波器（Kernel），通过在原始图像上平移来提取特征。
4. 池化（pooling）对图片进行压缩（降采样）。
5. 按照定义的 CNN 结构重复 1 和 2 步骤，通过中的各个卷积层和池化层。
6. 卷积和池化提取出了图像的特征，最后通过全连接（FC, Full Connection）作为分类器输出分类结果。

### 模型定义

构建神经网络，机器学习模型接受输入，然后产生输出。具体操作的含义已在代码注释中阐明。

```javascript
function getModel() {
  const model = tf.sequential();

  // 图像参数定义
  const IMAGE_WIDTH = 28;
  const IMAGE_HEIGHT = 28;
  const IMAGE_CHANNELS = 1;

  // 在卷积神经网络的第一层必须指定输入形状
  // 然后在该层中进行的卷积操作指定一些参数
  model.add(
    tf.layers.conv2d({
      inputShape: [IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS],
      kernelSize: 5,
      filters: 8,
      strides: 1,
      activation: "relu",
      kernelInitializer: "varianceScaling",
    })
  );

  // MaxPooling 层充当一种下采样，使用区域中的最大值而不是取平均值。
  model.add(tf.layers.maxPooling2d({ poolSize: [2, 2], strides: [2, 2] }));

  // 重复另一个 conv2d + maxPooling 操作
  model.add(
    tf.layers.conv2d({
      kernelSize: 5,
      filters: 16,
      strides: 1,
      activation: "relu",
      kernelInitializer: "varianceScaling",
    })
  );
  model.add(tf.layers.maxPooling2d({ poolSize: [2, 2], strides: [2, 2] }));

  // 将2D滤波器的输出展平为1D向量，以准备将其输入到最后一层（为分类层做准备）
  model.add(tf.layers.flatten());

  // 我们的最后一层是一个密集层，其中包含10个输出单元，
  // 每个输出类别一个单元（即0, 1, 2, 3, 4, 5, 6, 7, 8, 9）
  const NUM_OUTPUT_CLASSES = 10;
  model.add(
    tf.layers.dense({
      units: NUM_OUTPUT_CLASSES,
      kernelInitializer: "varianceScaling",
      activation: "softmax",
    })
  );

  // 选择一个优化器，损失函数和精度度量，然后编译并返回模型
  const optimizer = tf.train.adam();
  model.compile({
    optimizer: optimizer,
    loss: "categoricalCrossentropy",
    metrics: ["accuracy"],
  });

  return model;
}
```

### 训练模型

```javascript
async function train(model, data) {
  const metrics = ["loss", "val_loss", "acc", "val_acc"];
  const container = {
    name: "Model Training",
    styles: { height: "1000px" },
  };
  const fitCallbacks = tfvis.show.fitCallbacks(container, metrics);

  const BATCH_SIZE = 512;
  const TRAIN_DATA_SIZE = 5500;
  const TEST_DATA_SIZE = 1000;

  const [trainXs, trainYs] = tf.tidy(() => {
    const d = data.nextTrainBatch(TRAIN_DATA_SIZE);
    return [d.xs.reshape([TRAIN_DATA_SIZE, 28, 28, 1]), d.labels];
  });

  const [testXs, testYs] = tf.tidy(() => {
    const d = data.nextTestBatch(TEST_DATA_SIZE);
    return [d.xs.reshape([TEST_DATA_SIZE, 28, 28, 1]), d.labels];
  });

  return model.fit(trainXs, trainYs, {
    batchSize: BATCH_SIZE,
    validationData: [testXs, testYs],
    epochs: 10,
    shuffle: true,
    callbacks: fitCallbacks,
  });
}
```

### 测试模型

```javascript
const classNames = [
  "Zero",
  "One",
  "Two",
  "Three",
  "Four",
  "Five",
  "Six",
  "Seven",
  "Eight",
  "Nine",
];

function doPrediction(model, data, testDataSize = 500) {
  const IMAGE_WIDTH = 28;
  const IMAGE_HEIGHT = 28;
  const testData = data.nextTestBatch(testDataSize);
  const testxs = testData.xs.reshape([
    testDataSize,
    IMAGE_WIDTH,
    IMAGE_HEIGHT,
    1,
  ]);
  const labels = testData.labels.argMax(-1);
  const preds = model.predict(testxs).argMax(-1);

  testxs.dispose();
  return [preds, labels];
}
```

### 结果示例

<div align="center">
	<img src="https://github.com/AbyssLink/pic/blob/master/custom/2018-12-18_02-56.png?raw=true" width="200px" alt="1" >
  <img src="https://github.com/AbyssLink/pic/blob/master/custom/2018-12-18_12-57.png?raw=true" width="200px" alt="2" >
</div>

### 将视频转换为图片数据集

使用 ffmpeg 将视频转换为一组图片，选取图片相似度比较算法，定义特定阈值过滤掉非常相似的图像（如相邻帧非常接近的两张图像）。得到的拆分图像可作为数据集供 CNN 训练。

## 基于 Node-RED 开发自定义节点

Node-RED 具有良好的拓展性，其内建的底层控制流暴露出了较丰富的 API 供开发者创建自定义节点。节点在部署流时创建，它们可以在流运行时发送和接收一些消息，而在部署下一个流时将删除它们，按照新的节点定义重新创建。阅读 Node-RED 的文档会发现，Node-RED 的自定义节点的创建和 Node.js 的 package 创建相似。每个节点由三个文件组成：

- nodeName.js，该文件定义了节点的运行时的行为，包括接收信息，处理信息，传送信息，记录事件等。
- nodeName.html，该文件定义了节点在编辑器中的显示方式，包括显示的节点名称，用户输入的对话框，以及侧边栏显示的帮助文本。

- package.json，Node.js 模块用来描述其内容的标准文件，实现 npm 管理，处理依赖关系，并将所有文件打包为一个模块。

**DHash 节点**

由于求图片的 Difference Hash 是一个异步操作，使用 async 和 await 关键字对进程进行同步。

**dhash.js**

```javascript
const { DHash } = require("./imageHash");

module.exports = function (RED) {
  function getDHash(config) {
    RED.nodes.createNode(this, config);
    var node = this;
    node.on("input", async function (msg) {
      msg.payload = msg.payload.imgPath;
      msg.payload.hash = await DHash(imgPath);
      node.send(msg);
    });
  }
  RED.nodes.registerType("lower-case", LowerCaseNode);
};
```

**dhash.html**

```html
<script type="text/javascript">
  RED.nodes.registerType("lower-case", {
    category: "input", //父标签
    color: "#a6bbcf",
    defaults: {
      name: { value: "" }, //向后端传值
    },
    inputs: 1, //输入口
    outputs: 1, //输出口
    icon: "file.png",
    label: function () {
      return this.name || "sample"; //显示标签名
    },
  });
</script>
...
```

**package.json**

```json
{
    "name" : "difference-hash",
    ...
    "node-red" : {
        "nodes": {
            "lower-case": "lower-case.js"
        }
    }
}
```
