# 移动应用开发及上线流程简单介绍

## 什么是移动应用？

移动应用是指设计给[智能手机](https://zh.wikipedia.org/wiki/智能手机)、[平板电脑](https://zh.wikipedia.org/wiki/平板電腦)或其他[移动设备](https://zh.wikipedia.org/wiki/移动设备)运行的一种[应用程序](https://zh.wikipedia.org/wiki/应用软件)。

移动应用（Mobile App）运行在移动操作系统（Mobile platform）上，开发中的移动操作系统有：

| 名称                  | 是否开放源码 | 平台                                                                                                           |
| --------------------- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| Android、Wear OS      | 是           | [智能手机](https://wiki.kfd.me/wiki/智慧型手機)和[平板电脑](https://wiki.kfd.me/wiki/平板電腦)与其他便携式设备 |
| iOS、iPad OS、watchOS | 否           | iPhone、iPod touch、iPad 及 Apple Watch                                                                        |
| Sailfish OS           | 是           | 少数几款移动设备                                                                                               |
| webOS                 | 是           | [电视](https://wiki.kfd.me/wiki/電視)等[家电](https://wiki.kfd.me/wiki/家電)产品                               |

References: [移动操作系统](https://wiki.kfd.me/wiki/行動作業系統)

## 移动应用开发流程

![](https://i.loli.net/2020/08/28/FRzbBSEgK5jCIVQ.png)

References: [Mobile App Development Process](https://www.invonto.com/insights/mobile-app-development-process/)

## 移动应用开发模式

目前移动应用的技术栈可以分成三类：原生 App，混合 App，跨平台 App。

### **1. 原生 App 技术栈**

原生技术栈（native technology stack）指的是，只能用于特定手机平台的开发技术。比如，安卓平台的 Java 技术栈，iOS 平台的 Object-C 技术栈或 Swift 技术栈。

<img src="https://www.godsgracetech.com/images/Native-Mobile-App-Development.png" style="zoom:50%;" />

示例应用：iOS 计算器、Reeder、LastPass 等。

### **2. 混合 App 技术栈**

混合技术栈（hybrid technology stack）指的是开发混合 App 的技术，也就是把 Web 网页放到特定的容器中，然后再打包成各个平台的原生 App。所以，混合技术栈其实是 Web 技术栈 + 容器技术栈，典型代表是 PhoneGap、Cordova、Ionic 等框架。

<img src="https://www.tigren.com/wp-content/uploads/2017/11/magento-2-mobile-app-magento-hybrid-app-native-app-web-app.png" style="zoom: 20%;" />

示例应用：淘宝、今日头条、微信（微信公众号、微信小程序）、印象笔记、推特、Gmail 等。

### **3. 跨平台 App 技术栈**

跨平台技术栈（cross-platform technology stack）指的是使用一种技术，同时支持多个手机平台。它与混合技术栈的区别是，不使用 Web 技术，即它的页面不是 HTML5 页面，而是使用自己的语法写的 UI 层，然后编译成各平台的原生 App。

这个技术栈就是纯粹的容器技术栈，React Native、Xamarin、Flutter 都属于这一类。

<img src="https://www.mindinventory.com/blog/wp-content/uploads/2019/11/cross-platform-frameworks-1200x500.png" style="zoom:45%;" />

示例应用：QQ、手机百度、手机京东、Facebook、Instgram、Tesla（React Native），闲鱼、腾讯 Now 直播（Flutter）等。

References: [H5 手机 App 开发入门](https://www.ruanyifeng.com/blog/2019/12/mobile-app-technology-stack.html)

### **三种开发模式比较表**

| 类型       | 原生(NATVIE)                                                                                | 混合(Hybrid)                                                 | 跨平台(cross-platform)                                          |
| ---------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| 开发工具   | XCode, Android Studio                                                                       | Ionic, Visual Studio                                         | React Native, Flutter                                           |
| 渲染引擎   | 原生                                                                                        | 浏览器                                                       | 原生                                                            |
| 开发难易度 | 😕                                                                                          | 🤔                                                           | 😏                                                              |
| 优点       | 完全访问设备功能<br/>强大的性能<br/>高质量功能和 UX<br/>访问所有本机 API 和特定于平台的功能 | 多操作系统支持<br/>代码重用<br/>成本效益<br/>强大的定制功能  | 多操作系统支持<br/>近乎原生的 UI 性能<br/>代码重用<br/>成本效益 |
| 缺点       | 无多平台支持<br/>如需多操作系统支持则开发成本较高<br/>没有代码重用                          | 性能较慢<br/>操作系统功能访问受限<br/>不能与其他本机应用交互 | 性能较慢<br/>操作系统功能访问受限<br/>与其他本机应用程序交互差  |

References: [Mobile App Development Approaches Explained](https://railsware.com/blog/native-vs-hybrid-vs-cross-platform/)

## 移动应用开发相关技术

### WebView 控件

通常情况下，App 内部会使用 WebView 控件作为网页引擎。这是系统自带的控件，专门用来显示网页。应用程序的界面，只要放上 WebView，就好像内嵌了浏览器窗口，可以显示网页。

![](https://i.loli.net/2020/08/28/ni8VwkdqI6HoB9E.jpg)

不同的 App 技术栈要显示网页，区别仅仅在于怎么处理 WebView 这个原生控件。

- 原生技术栈：需要开发者自己把 WebView 控件放到页面上。
- 混合技术栈：页面本身就是网页，默认在 WebView 中显示。
- 跨平台技术栈：提供一个 WebView 的语法，编译的时候将其换成原生的 WebView。

### 微服务

**微服务** (Microservices) 是一种[软件架构风格](https://zh.wikipedia.org/wiki/软件架构)，它是以专注于单一责任与功能的小型功能区块 (Small Building Blocks) 为基础，利用模块化的方式组合出复杂的大型应用程序，各功能区块使用与语言无关 (Language-Independent/Language agnostic) 的 API 集相互通信。

References: [微服务](https://zh.wikipedia.org/zh-cn/微服務)

以微信为例，腾讯在介绍微信微服务架构的论文中写道，微信将其微服务分类为“入口跳转”服务（用于接收外部请求的前端服务）、“共享跳转”服务（中间层协调服务）以及“基本服务”（不向任何其它服务暴露，因此可充当请求接收方的服务）。

![](https://i.loli.net/2020/08/28/L5nKeTSXlD4dfk6.jpg)

References: https://www.cs.columbia.edu/~ruigu/papers/socc18-final100.pdf

## 移动应用架构示例

### 微信

#### 前台架构

![](https://static001.infoq.cn/resource/image/13/1e/13579dfda32fe8948d4fa3745bbfb11e.png)

#### 后台架构

![](https://i.loli.net/2020/08/28/Nt1HTmBErdXu2kQ.png)

References: https://cloud.tencent.com/developer/article/1445567

## 如何发布移动应用

### iOS 应用发布方式

| 发布方式   | 说明                                                                                                                                    |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| App Store  | Apple 目前唯一的官方应用商店，需要 Apple 审核                                                                                           |
| TestFlight | Apple 的内测应用商店，可通过电子邮件分发下载链接<br />外部人员测试需 Apple 审核（上限 2000 人）<br />内部人员测试无需审核（上限 25 人） |

### Apple 开发者账号对比

| 类型               | 费用        | App Sotre 上架 | 需要 DUNS Number | 说明                                                                                                      |     |
| ------------------ | ----------- | -------------- | ---------------- | --------------------------------------------------------------------------------------------------------- | --- |
| 个人（Individual） | 99\$ / year | 是             | 否               | 个人和公司账号只能上架 App Store 供用户下载。<br />如果发布 APP 到自己服务器，最多只支持 100 台手机安装。 |     |
| 公司（Company）    | 99\$ / year | 是             | 是               | 和个人版的不同：允许多个开发者进行协作开发，可以设置多个 Apple ID                                         |     |
| 企业（Enterprise） | 299\$ /year | 否             | 是               | 无法上架 App Store 只能通过自己的服务器或者三方平台安装，只能企业内部使用，否则有被封号的风险。           |     |

References:

[Distributing your App](https://developer.apple.com/documentation/xcode/distributing_your_app_for_beta_testing_and_releases)

[Code Signing](https://developer.apple.com/support/code-signing/)

[Apple 开发者账号介绍及证书配置说明](https://www.jianshu.com/p/8190cf4a8172)

### 向 App Store 发布应用前

1. 测试应用是否有奔溃和错误
2. 确保所有应用信息和元数据完整且准确
3. 提供有效的演示账户和登陆信息
4. 启用后端服务，保证在审核期间处于活动状态
5. 检查应用是否遵循特定文档的指导，如：
   1. 人机界面准则
   2. 营销资源和身份准则
   3. Apple 支付身份准则

References: [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)

### 在 App Store 发布

1. 生成应用程序 ID
2. 在 XCode 中建立档案
3. 设置 App Store Connect:
   1. 创建新应用
   2. 填写应用信息
   3. 确定价格和供货量
   4. 提交审查
4. 创建支持和隐私协议网站
5. 提交审查，等待发布

References: [how to publish app to app store](https://blog.usejournal.com/how-to-publishing-an-app-to-the-app-store-2019-guide-1c73a582136c)

### Android 应用发布方式

| 发布方式                             | 说明                                                                       |
| ------------------------------------ | -------------------------------------------------------------------------- |
| 应用市场                             | 如 Google Play，各大安卓厂商定制的应用市场，可同时在多个市场中分发         |
| 网站或服务器（包括私人和企业服务器） | 用户需要允许安装位置来源的应用<br />无法使用许可服务来组织他人未经授权使用 |

### 向 Android 应用市场发布应用前

1. 查看核对清单以规划发布
2. 选定合适的受众群体和设备类型
   1. Android 设备
   2. Android Wear、Android TV、Android Auto 平台
3. 测试应用
   1. 发布测试报告和奔溃报告
   2. 测试应用的每个语言版本
   3. 监控统计数据以发现非预期的变化

References: [Android Developer: Distribution](https://developer.android.com/distribute/best-practices/launch?hl=zh-cn)

### 在 Android 应用市场发布

**在 Google Play 发布：**

1. 注册 Google Play 开发者账号
2. 接受开发者分发协议
3. 缴纳注册费
4. 完善账号详细信息
5. 使用 play 管理中心
   1. 上传应用
   2. 设置定价和分发番位
   3. 设置开放式测试、封闭式测试或内部测试
   4. 查看报告、统计信息和评价

References: [如何使用 Play 管理中心](https://support.google.com/googleplay/android-developer/answer/6112435?hl=zh-Hans)

**在华为应用市场发布：**

1. 注册登录华为开发者联盟并通过实名认证。
   进入应用市场管理页面发布新应用，填写应用信息并上传 APK。
2. 选择语言设置，完善应用基础信息设置。
3. 选择付费情况，勾选需要分发的国家及地区，并填写隐私声明链接。
4. 检查产品包信息、分发信息和基础信息是否正确。
   确认无误点击提交完成新应用上传。

References: [华为应用分发流程](https://developer.huawei.com/consumer/cn/doc/distribution/app/agc-create_app)
