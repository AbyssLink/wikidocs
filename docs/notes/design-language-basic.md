# 设计语言简单介绍

设计语言(英语：Design Language)是系统化和明确规范的语言，应用于数字产品、用户界面设计、工业设计中。

- **对于设计师**：设计语言可以统一不同的表达方式、偏好、或风格。

- **对于团队**：设计语言可以让团队投入更多精力到问题本质，提升协作效率。

- **对于用户**：设计语言可以让产品表现保持一致，提升产品的识别度。

## 数字产品设计原则

### 三大通用原则

**1、Clarity（清晰）：**文字要清晰易读，图标要精确醒目

**2、Deference（遵从）：**设计要服从内容，勿过度设计

**3、Depth（深度）：**布局层次分明，交互动画生动

总结来说：设计语言需要有统一界面元素和交互方式，要向用户清楚直观地传达信息，引导用户进行交互但不能剥夺用户的控制权，并给予用户的良好的操作反馈和结果。

来源：[iOS human interface guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/overview/themes/)

## 目前流行的数字产品中著名的例子

- 谷歌公司：质感设计（Material Design）
- 苹果公司：扁平化设计（Flat Design）
- 微软公司：流畅设计体系 (Fluent Design)
- 阿里公司：蚂蚁金服设计 (Ant Design)
- 火狐：光子设计系统（Photon Design System）
- 锤子科技：Smartisan OS UI

| Name                        | PREVIEW                                                                                                                                                                                                                                                     | LINK                                                                                                    |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Google Material Design      | ![](https://i.loli.net/2020/09/11/JFpWZHqdlR3PjhQ.png)                                                                                                                                                                                                      | [Materil IO](https://material.io/design/introduction#design)                                            |
| Apple Flat Design           | ![](https://i.loli.net/2020/09/11/3McAXtOwVCzfZJl.png)                                                                                                                                                                                                      | [iOS Design Themes](https://developer.apple.com/design/human-interface-guidelines/ios/overview/themes/) |
| Microsoft Fluent Design     | ![](https://assets.materialup.com/uploads/1cdf218d-400a-4b9b-8cbf-b93cda26a27e/preview.jpg)                                                                                                                                                                 | [Fluent Design System](https://www.microsoft.com/design/fluent/#/)                                      |
| Alibaba Ant Design          | ![](https://camo.githubusercontent.com/885b0f01379dbbcbbbad315c6290ba1394f12cc5/68747470733a2f2f67772e616c697061796f626a656374732e636f6d2f6d646e2f726d735f3038653337382f616674732f696d672f412a596c3833524a685545376b4141414141414141414141426b4152516e4151) | [Ant Design](https://ant.design/)                                                                       |
| Firefox Photo Design System | ![](https://i.loli.net/2020/09/11/eE7PjomYMSwg1Hd.png)                                                                                                                                                                                                      | [Photon Design System](https://design.firefox.com/photon/welcome.html)                                  |
| Smartisan OS UI             | ![](https://i.loli.net/2020/09/11/mCzgf86bsPtoQMO.jpg)                                                                                                                                                                                                      |                                                                                                         |

## 设计语言对比

设计语言的主题主要起源于三个方向：拟物和扁平和中性。

### 从拟物（Skeuomorphism design）到扁平（Flat Design）

<img src="https://i.loli.net/2020/09/11/2uJNGiFqz5XkLgl.png" style="zoom:50%;" />

这种设计更改的一个示例是从拟态 UI 设计到扁平 UI 的更改。要更广泛地了解这种拟态，就是软件中的对象模仿其真实世界中的对象。而扁平设计是一种简约的用户界面设计。

扁平化设计更加注重简洁性，应用程序可能没有渐变，阴影和效果，可提供干净清晰的用户体验。由于它具有极少的美观性，因此它鼓励设计人员更加重视对象，按钮信息和颜色信息的层次结构。功能是此设计方法的核心方面，它使用户体验变得更加有效和实用。与应用程序的设计相比，用户将更加专注于目的或目标。这使用户能够按预期使用产品。

### Material Design

Google 为 Android 和 Web 提供的设计语言。目的是创造一种连贯，实用和可访问的视觉语言。

目的是设计基于触摸屏的 Web 和移动体验，并充分利用触摸屏的优势，并从纸和墨水中汲取灵感。

<img src="https://i.loli.net/2020/09/11/JFpWZHqdlR3PjhQ.png" style="zoom:50%;" />

材料设计的目的是将扁平设计和拟形设计两者结合在一起。像扁平设计一样，Material Design 也旨在使用大胆的颜色和 2D 图像，但是其目的是部署图形和具有特点的 UI，以从基于打印的设计中汲取灵感。

![](https://i.loli.net/2020/09/11/qhYRHFKEbvmrLPk.png)

| 名称                            | ADVANTAGE                                                                                                                     | DISADVANTAGE                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 拟物设计 (Skeuomorphism design) | 1. 模拟现实中的 3D 图像，认知学习成本低<br />2. 视觉效果和交互效果直观                                                        | 1. 大多数的拟物界面和功能并无关联，只实现了视觉上的阴影和质感效果。<br />2. 随着数码科技的发展，拟物化的好处越来越少，随之带来的是开发成本增加。 |
| 扁平设计(Flat Design)           | 1. 整洁，无干扰的设计，可读性高，字体清晰 <br />2. 可以轻松调整以进行响应式设计 <br />3. 更优秀的性能表现，更快的应用加载速度 | 1. 缺乏深度，使元素看起来不太可点击<br />2. 较严格的设计准则，限制了创意的实现                                                                   |
| 质感设计(Material Design)       | 1. 统一而简单的界面<br />2. 原则和目标为设计师提供了一致性 <br />3. Z 轴的设计产生深度，使用直观                              | 1. 在没有动作的情况下，设计的 UI 通常缺乏直观性。<br />2. 浮动按钮等元素交互层级深，不直观。                                                     |
