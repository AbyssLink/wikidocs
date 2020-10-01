# ASUS 路由器体验

## 关于路由器

**品牌分级**

一：网件, 华硕, Linksys(不推荐)

二：斐讯, D-link, TP-LINK、腾达、水星、迅捷

三：华为（民用）、小米、360 等

[CPU 比较](https://www.notion.so/0972fe0e027c431ab40958097169927f)

## 开箱

原先家里用的 PHICOMM K2P 爆出隐私问题(流量劫持，后台记录历史)且因版本原因无法刷机。

刚好家里移动升到 200M 宽带，想着换一台质量好些的路由器，

于是选择了比较均衡的 **ASUS RT-ACRH17:**

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_135718.jpeg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_135718.jpeg)

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_135641.jpeg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_135641.jpeg)

路由器比想象中的小，外观感觉还挺好看。

## 信号测试

**Wi-Fi 环境分析**

使用 **Acrylic WiFi Professional。**

专业 WiFi 分析软件，界面非常友好，个人版本免费。商用版本 5 天试用期。

**基本信息**

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144220.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144220.jpg)

ASUS RT-ACRH17

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144239.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144239.jpg)

PHICOMM K2P

**综合评分**

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144856.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144856.jpg)

ASUS RT-ACRH17

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144720.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_144720.jpg)

PHICOMM K2P

为啥 ASUS 的密码安全等级低啊，明明用的一样的加密方式...不懂

**Wi-Fi 测速**

**SpeedTest.net。**网速测试工具，不过好像具体数字和测速点关系很大...

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_110752.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_110752.jpg)

测试结果从下到上分别为测速点 1~4:

左图为户型图和测速点

(KeyNote 绘制)

仅测试 5G Wi-Fi 速度。

设备: iPhone 6s Plus

软件: SpeedTest app

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_134513.jpeg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_134513.jpeg)

ASUS RT-ACRH17

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_134527.jpeg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-10-2020_134527.jpeg)

PHICOMM K2P

## USB 存储

准备拆下家里的闲置笔记本做移动硬盘，等硬盘盒快递。

好吧，闲置笔记本是 07 年的 ThinkPad，硬盘接口不是 SATA，用不上了。

协议默认是 2.0 的，估计是防止对 2.4G 无线的干扰。

需要注意的是，外置 USB 磁盘只支持 MS-DOS, FAT, NTFS 格式 (ex-FAT 默默留下了眼泪)

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-11-2020_234158.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-11-2020_234158.jpg)

挂载成功后再设置中打开网络服务器，就能在 Finder 的 Network 选项卡中看到网络磁盘了。

(吐槽下 Mac 给的图标真古老...大屁股机)

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-11-2020_234611.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-11-2020_234611.jpg)

默认登陆的用户名和密码就是后台管理员登陆的用户名和密码。

登陆成功后就可以访问磁盘的内容。

实测访问速度比较捉急，也就勉强看 1080p 视频的水平，打开大一点的图片都卡，可能和 U 盘 USB 2.0 的接口有关，未来还是老老实实用 NAS 吧...

## 问题

最近经常遇到 ASUS_ACRH17 5G 频段断连的问题，Log 如下：

    Mar 15 19:40:03 kernel: Switching to Tx Mode-1 Threshold 280
    Mar 15 19:41:38 kernel: Switching to Tx Mode-1 Threshold 0
    Mar 15 19:41:41 kernel: Switching to Tx Mode-1 Threshold 280
    Mar 15 19:45:50 kernel: SmartLogEvent: STA KICKOUT SUBEVENT
    Mar 15 19:45:51 kernel: SmartLogEvent: STA KICKOUT SUBEVENT

查到的解决方案有：

1. 设置固定信道，尽量不和别屋的无线信道冲突
2. 固定信道频段为 80Mhz
3. 刷回旧版固件

目前测试方法 1、2 无效，刷回旧版固件信号断流有好转。

历史固件下载地址：

[RT-ACRH17 BIOS & FIRMWARE | Networking | ASUS Global](https://www.asus.com/Networking/RT-ACRH17/HelpDesk_BIOS/)

Last Saturday
今天在群里有人讨论 Wi-Fi 延迟，于是我也跟着测了一下：

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-21-2020_211438.jpeg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-21-2020_211438.jpeg)

群友的

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-21-2020_211453.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-21-2020_211453.jpg)

我的

？？？这样一比俺的延迟也太严重了吧！没办法，只好去 ASUS 官网下回旧版固件(官网固件文件有 md5 校验信息，好评)，重新刷回旧版后的延迟：

![https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-21-2020_211813.jpg](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/03-21-2020_211813.jpg)

达不到群友的延迟水平但至少好一些了吧...看后台也不会经常报上面的错误信息了。再用几天看看。

Last Sunday
好吧，延迟小了却还是同样的报错，我尝试一下刷回最初始的固件吧。

参考：

[5Ghz help! ASUS RT-ACRH17](https://www.reddit.com/r/HomeNetworking/comments/dpcmhw/5ghz_help_asus_rtacrh17/)

[大家好，我是来给你家 WiFi 提速的](https://zhuanlan.zhihu.com/p/50513681)

## 软路由

wait.

## 参考

[2019 双 11 选购攻略，2020 年也适用！-路由器交流](https://www.acwifi.net/8322.html)

[你了解你的网络吗--7 款网络测试工具简介，帮你优化家庭组网*值客原创*什么值得买](https://post.smzdm.com/p/a3gzwe4k/)

[升级电信两百兆宽带！全家欢享智能家庭千兆网络：ASUS 华硕 RT-ACRH17 无线路由器 简评*值客原创*什么值得买](https://post.smzdm.com/p/612332/)

[路由器中的战斗机-网件 R7000P 路由器体验分享*值客原创*什么值得买](https://post.smzdm.com/p/akm7vqr8/)

[鸟枪换炮：NETGEAR 美国网件 R7000 路由器让半个小区知道你 附带刷梅林固件*值客原创*什么值得买](https://post.smzdm.com/p/700720/)

[绝对值得买 篇二：家庭 WiFi 布网实战，极致性价比！618 的绝对值路由器，买到就是赚到！*值客原创*什么值得买](https://post.smzdm.com/p/akmrrdgr/)
