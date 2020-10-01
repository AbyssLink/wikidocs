# 斐讯 K2 刷入固件

拼夕夕花了 83 元新买了台斐讯 k2，经过大佬的帮助刷入了潘多拉固件，成功破解了闪讯的限制。简要的记录下过程备用：

软件版本： 22.5.11.5
设备型号： K2
硬件版本： A2

路由器刷固件的过程分为两步：

1. 刷入 breed
2. 在 breed 的控制页面中刷入特定固件

**create time: 2018.11.06**

**last test success: 2019.05.09**

## 刷入 breed

breed 类似 uboot，用于路由器的引导，刷了 breed 后，可以方便的刷第三方固件

参考自：http://www.right.com.cn/forum/thread-325258-1-1.html

### 1. 开启 telnet

对斐讯最新 K2 新版 22.6.511.69 ，需开启 telnet 刷 breed，其实就是定时重启漏洞变为定时更新漏洞

1. 路由器上电，电脑或手机连接路由器热点，浏览器访问` 192.168.2.1` , 进入路由设置页面 -> 高级设置-> 自动升级 -> 自定义升级时间-> 开启;

2. 点选时间中的右侧下拉分钟选择框，鼠标箭头放在 05 上，点击鼠标右键，在 Firefox 或傲游或 chrome 中 “审查元素”：

3. 双击"05"，改为你要执行的命令：

改为：

```js
05 | (/usr/bins / telnetd - l / bin / login.sh);
```

在定时重启路由器页面上重新选择 05 之后（这里要注意，一定要重选，并且重选后可以看到 05 后面自己输入的字符）：

点击保存，就可以开启 telnet，通过其他终端连接到路由器。

### 2. 刷入 breed

参考自：http://www.right.com.cn/forum/thread-208753-1-1.html

​ http://www.iytc.net/wordpress/?p=1624
注：以上方法在 2019.05.09 测试失效

**这步很关键，刷 breed 相当于 android 的 twrp，可以帮助用户安装第三方固件，并有效地防止路由器变砖！**

1. windows 命令行程序 telnet 登陆到路由器控制台，再输入如下语句即可刷入 breed（版本为 20180805）：

```shell
wget http://iytc.net/down/k2_breed.sh -O -|sh
```

​ 本固件集成了最新的 breed，刷入后自动将 bootloader 更新为最新 breed。进行操作后，路由器会写 breed 并重启。如果路由器没有自动重启，说明操作过程有误，请仔细检查操作过程。

### 3.进入 Breed

1. 拔除 K2 上 Wan 口的网线，路由器断电，**持续按住**路由器上的 reset 按钮，接通路由器电源，3 秒后松开 reset 按钮。
2. 将 **Wan 口与你的电脑网口** 连接，在浏览器地址栏输入“http://192.168.1.1”访问Breed Web。
3. 进入 Breed Web 后，请及时进行原始 EEPROM、固件备份，然后再刷其他的固件。

## 4. 刷入固件

开刷前，请必须记得先「恢复出厂设置」->「Config 区 (公版)」，然后点「执行」

![img](https://upload-images.jianshu.io/upload_images/3943248-f9504e433299dc24.png?imageMogr2/auto-orient/strip|imageView2/2/w/650)

固件下载地址：http://www.right.com.cn/forum/thread-161324-1-1.html

(点击「恢复固件」->固件->浏览，选中你下载好的 K2 的固件文件，比如我这次是「RT-AC54U-GPIO-1-PSG1218-64M_3.4.3.9-099.trx」，点击「上传」即可)

1. 选择对应的路由器型号的固件下载并刷入。

2. 成功刷入固件后，连接路由器网络，浏览器输入：192.168.123.1，进入路由器控制台 (如要求验证，默认用户名：admin，密码：admin)，即可看到如下图的潘多拉管理页面。

![img](https://www.right.com.cn/forum/data/attachment/forum/201805/12/091415djuuqyy9n0uzhu8u.png)

3. 外部网络中可安装各种工具，如闪讯破解工具，破除其一人一号的限制。
