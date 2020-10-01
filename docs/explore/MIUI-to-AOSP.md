# 小米 MIUI 转类原生 过程记录

本文记录 MIUI 转向类原生系统的流程。

## 为什么放弃 MIUI

> - MIUI 预装软件多且无法删除，功能臃肿
> - MIUI 恼人的广告
> - MIUI 服务和 Google 的服务重复或冲突
> - MIUI 不能获得完整 Root 权限
>
> - 小米 📱, 为刷机而生！ (误

当然， MIUI 的驱动支持和性能表现都比类原生系统好很多。

类原生系统一般由开源组织维护，在驱动和软件适配上易产生问题。

## 名词介绍

- **Bootloader**: 在 Android 操作系统运行之前运行的一段代码。Bootloader 必须先解锁，才能引导除了预装系统以外的系统
- **ROM(Read Only Memory)**: 包含 Android 操作系统和执行指令(系统映像)的文件
- **刷机**: 将 ROM 文件...安装到手机的过程
- **卡刷/线刷**: 使用手机内置存储卡刷机 / 使用数据线连接 PC 刷机
- **Fastboot**: 刷机模式，用于线刷
- **Recovery**: 恢复模式，用于卡刷
- **TWRP(Team Win Recovery Project)**: 一个开源的第三方 Recovery，支持写入自定义系统镜像
- **类原生系统**: 类似 Andorid 原生的系统，基于 Android Open Source Project (AOSP)

## 流程

### 0. 准备设备

- 小米手机
- 电脑
- 数据线

### 1. 解锁 Bootloader

1. 为小米账号申请解锁资格：https://www.miui.com/unlock/index.html

   首次申请一般需要等待几天的时间审核（最近审核时间越来越长了...)

   审核通过后，下载解锁工具，开始解锁吧。

![img](https://upload.cc/i1/2018/07/07/VEp6lX.jpg)

2. 在电脑上运行小米解锁工具，登陆小米账号。

3. 手机关机，同时按住 `开机键` 和 `音量下键` 进入 FastBoot 模式，使用数据线连接电脑
4. 这时电脑应该会识别出设备。点击屏幕上的 “解锁”按钮，等进度条走完你的手机就解锁了。
5. 重启手机，屏幕底部会显示一个 Unlocked（已解锁）的标识。

### 2. 刷入 TWRP

1. 手机关机，同时按住 `开机键` 和 `音量下键` 进入 FastBoot 模式，使用数据线连接电脑 (接下来几步在电脑上操作)

2. 下载符合手机机型的 TWRP 镜像文件: https://twrp.me/Devices/

3. 下载 Google 提供的 [android-platform-tools](https://developer.android.com/studio/releases/platform-tools)，解压缩

4. 将 TWRP 镜像文件复制到 android-platform-tools 文件夹下，重命名为 `recovery.img`

5. 打开终端，依次输入如下命令

   ```shell
   # 显示设备状态
   $ fastboot devices

   # 刷入 TWRP
   $ fastboot flash recovery recovery.img
   ```

6. 输入上述命令后，手机原生的 Recovery 会被 TWRP 所覆盖

7. 手机关机，同时按住 `开机键` 和 `音量上键` 进入 TWRP 模式

### 3. 安装 ROM

0. **选择 ROM**：到 XDA 论坛 (全球最大的 Android 交流论坛)：https://forum.xda-developers.com

   ![](https://tva1.sinaimg.cn/large/006tNbRwly1g9xrlez94sj31c00u0b29.jpg)

   搜索你的机型对应的 ROM，这些 ROM 大多基于开源的 AOSP 项目编译，由开发者个人或社区进行维护。

> 由于不同的 ROM 安装方法都是大同小异的，就不赘述了 🤣

| ![Screenshot_20181125-164155](https://tva1.sinaimg.cn/large/006tNbRwly1g9xtrj38grj30u01hc0yl.jpg)                                                                        | ![Screenshot_20190207-173535](https://tva1.sinaimg.cn/large/006tNbRwly1g9wsr4m5u5j30u01ny0xt.jpg)          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| ![Screenshot_20190204-090313](https://mokee-discourse.s3.dualstack.ap-northeast-1.amazonaws.com/optimized/2X/1/1073ec9290653316f52c517ee21e4c429ef75b06_2_562x1000.jpeg) | ![Screenshot_Settings_20181125-164802](https://tva1.sinaimg.cn/large/006tNbRwly1g9xtri5yf7j30u01hctdb.jpg) |

### 4. 跳过开机验证

由于原生系统首次开机时需要向 Google 发送本机验证消息，但此时并没有科学辅助工具。

解决方案 1：https://vitan.me/2018/05/04/Win10-Share-WiFI/

(2019.05.13 更新)解决方案 2：https://www.v2ex.com/t/485478

即在 TWRP 中挂载 system 分区，用 vi 编辑 build.prop ，加一句 ro.setupwizard.mode=DISABLED

进入系统之后就开始享受吧…

### 5.开启 Google Feed (可选)

请参考这篇教程：https://bbs.mokeedev.com/t/topic/10903

### 6. 常见问题

> 问题描述：
>
> 先前刷了 havoc 的 rom, 今天进了一次 twrp 后不管再进 rom 和 twrp 触摸屏幕都失灵了。
> 我尝试在 fastboot 中格式化了 system data cache 分区，并线刷了 miui10 ，但重启后触屏仍然不能工作，可能是什么原因？
>
> 解决方案：
>
> 触控失灵有可能是修改后的 TWRP 导致的，推荐使用上文提到的官方 TWRP。若触控失灵，可以考虑线刷 miui 最新稳定版，一般能够修复。

### 7. 风险？

上述刷机操作基于 Recovery 模式，对 System、Cache、Data 等分区进行操作，不涉及用于系统引导的 Bootloader。

一般来说，只要手机能进入 Fastboot 模式，那么无论是装 TWRP 进入恢复模式进行卡刷，还是直接在 Fastboot 模式下线刷，都能轻松的将 Android 手机重装系统

> 但是，如果手机进入不了 Fastboot 模式了....那么，就和 Windows 系统进入不了 Bios 一样，基本没有刷入系统的可能了，这时候的手机一般就被认为是 🧱 了。遇到这种情况只能去售后...

## 总结

~~其实刷机不为调试的话没啥意思，日用还是 iOS 养老舒服 (苦笑)~~

## 外部链接

酷安网：https://www.coolapk.com

MOKEE: https://bbs.mokeedev.com

XDA: https://www.xda-developers.com

## 参考

https://bbs.letitfly.me/d/743

http://www.oneplusbbs.com/thread-3941475-1.html
