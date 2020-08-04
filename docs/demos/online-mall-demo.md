# 电子商城 demo

基于 Vue 和 Spring Boot 的一个电子商城

## Code

Front-end: (Deleted)
Back-end: https://github.com/AbyssLink/spikeproject

### 运行截图

| ![Screenshot 2019-06-17 at 9.44.43 PM](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00001.jpg) | ![Screenshot 2019-06-17 at 9.44.43 PM](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00002.jpg) |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| ![s3](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00003.jpg)                                  | ![Screenshot 2019-06-17 at 9.03.38 PM](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00004.jpg) |
| ![s6](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00005.jpg)                                  | ![s5](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00006.jpg)                                  |

### 项目介绍

这是一个简单的电子商城 demo，可以供普通用户和和管理员使用。

**普通用户权限:**

1. 查看商品
2. 购买商品(添加订单)
3. 查看、更新、删除自己的订单
4. 查看、更新个人信息
5. 查看商品的评论
6. 对商品添加评论
7. 更新、删除自己的评论

**管理员权限：**

1. 查看商品
2. 添加、更新、删除商品
3. 查看、更新、删除自己的订单
4. 查看、删除所有用户的订单
5. 查看、更新个人信息
6. 查看、更新、删除所有用户的信息
7. 查看商品的评论
8. 对商品添加评论
9. 更新、删除所有人的评论

关于订单下单、用户手机号注册等服务需要依赖第三方平台，所以没有具体实现，仅做了服务的数据模拟。

### 项目实现

项目的前端总体实现比较简单，由于 vuetify 本身就是已经非常成熟的响应式框架，我在样式和布局上主要通过修改一些组件的预设完成，主要的工作量在于前后端跨域请求数据和前端的用户状态管理问题。

#### 技术栈

`Vuetify` + `Vue` + `axios` + `Springboot` + `mybatis` + `mysql` + `redis`

#### 前端依赖库

1. 组件样式: `vuetify`, `material-design-icons-iconfont`

2. 全屏幕显示: `screenfull`

3. 图表：`vue-echarts`

4. 地图: `vue-baidu-map`

5. 路由处理: `vue-router`

6. 状态保存: `vuex`

7. ajax 请求: `axios`

8. 时间处理: `moment`

#### 后端依赖库

1. 全栈应用程序框架和控制反转容器实现：`Spring-boot`
2. 数据库连接/连接池管理：`mysql-connector-java`
3. druid 数据源: `com.alibaba.druid`
4. Mybatis 对 Spring-boot 支持: `mybatis-spring-boot-starter`
5. Redis 对 Spring-boot 支持: `spring-boot-starter-data-redis`
6. 校验类: `hibernate-validator`
7. 时间类: `joda-time`
8. 单元测试：`junit`
9. Spring-boot 测试：`spring-boot-starter-test`
10. mybatis 映射自动生成插件: `mybatis-generator-maven-plugin`

#### 数据库表结构定义

使用了 MySQL 数据库。

表结构定义比较简单，主要用到的的表有 **用户, 商品, 订单, 评论, 活动** 表，有如下注意点：

1. 为了安全和加密，将用户信息和用户密码分为两张表，使用 userId 进行管理，用户密码表中仅存储哈希加密后的用户密码。
2. 商品的库存由于受频繁出入库影响，更新频率很高，因此单列出一张**商品库存表**用于更新库存信息节约服务器资源。
3. 评论的属性没有设置外键，这样在删除商品和用户时评论仍会保留。
4. 数据库的所有属性都设置了**默认值**，这样可以大大减少 Java 后端中由于属性为空而产生 NullException 的风险。

##### ER 图

| Navicat 生成                                                                                                                 | DBeaver 生成                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ![Screenshot 2019-06-17 at 10.40.43 PM](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00009.jpg) | ![s2](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00010.jpg) |

#### 数据访问对象(DAO)

使用了 MyBatis 持久化框架。

MyBatis 通过 XML 描述符或注解把对象与存储过程或 SQL 语句关联起来, Spring-boot 中提供了 Mybatis 自动生成 XML 映射文件与 DAO 对象的插件：`mybatis-generator-maven-plugin`, 可以生成一些基本的数据库操作方法，为快速开发提供了很多的便利。添加自定义方法时模仿默认的 xml 格式即可。

#### 数据模型和视图对象(Model & VO)

定义 Model 层主要处理逻辑 Service 内的逻辑，并对 DAO 的方法进行封装。

定义 VO 层主要用于包装给前端的响应数据，主要用于前端视图的显示。

封装的目的：为不同的应用场景创建不同的对象，防止外部操作或内部错误使对象的产生污染。

#### 类自动注入与事务管理

使用了 SpringBoot 实现了类的自动注入与事务管理。

SpringBoot 其设计目的是用来简化新 Spring 应用的初始搭建以及开发过程，默认配置了很多框架的使用方式。

第一次我尝试使用的是 Spring 和 Spring MVC，其项目的配置流程为：

1. 配置 web.xml，加载 Spring 和 Spring mvc

2. 配置数据库连接、配置 Spring 事务

3. 配置加载配置文件的读取，开启注解

4. 配置日志文件
5. 配置完成之后部署 Tomcat 调试

而 SpringBoot 只需要在核心配置文件 application.properties 中配置：数据源信息、启动端口等。其他的类文件中一般只需通过注解就可完成管理(不用写比较难读的 XML 了)，且 SpringBoot 自带了一个 tomcat 服务器，不需要额外配置 tomcat ，也自带了单元调试的插件支持， 简化了项目配置的难度。

#### 定义统一返回类

前端在向后端发出请求时，后端返回的信息中需要包括两部分信息：

1. 操作是否成功
2. 返回的数据或错误信息

因此，为所有的 **Controller** 中的接口定义了一个统一返回类，规范给前端的信息:

```java
public class CommonReturnType {
    // 表明对应请求的处理返回结果 "success" 或 "fail"
    private String status;
    // 若 status = success, 则 data 返回前端需要的 json 数据
    // 若 status = fail, 则 data 返回通用的错误码格式(使前端可以获得有意义的错误信息)
    private Object data;

    // 定义一个通用的创建方法
    public static CommonReturnType create(Object result){
        return CommonReturnType.create(result, "success");
    }
    // *函数重载，返回数据和状态码
    public static CommonReturnType create(Object result, String status){
        CommonReturnType type = new CommonReturnType();
        type.setStatus(status);
        type.setData(result);
        return type;
    }
}
```

#### 前后端跨域实现

axios 默认跨域不带 cookies, 需要更改设置以完成跨域请求:

```javascript
import Axios from "axios";

// 设置 request 格式
Axios.defaults.withCredentials = true; //! 跨域带cookies
Axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";
Axios.defaults.headers.get["Content-Type"] =
  "application/x-www-form-urlencoded";

Vue.prototype.$http = Axios; // 再修改原型链，以全局使用
```

后端设置允许跨域：

```java
@Configuration
public class CORSConfig {
    @Bean
    public FilterRegistrationBean corsFilter() {
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowCredentials(true);
        // 设置你要允许的网站域名，如果全允许则设为 *
        // config.addAllowedOrigin("*");
        config.addAllowedOrigin("http://localhost:3000");
        // 如果要限制 HEADER 或 METHOD 请自行更改
        config.addAllowedHeader("*");
        config.addAllowedMethod("*");
        source.registerCorsConfiguration("/**", config);

        FilterRegistrationBean bean = new FilterRegistrationBean(new CorsFilter(source));

        bean.setOrder(0);
        return bean;
    }
}
```

#### 存储用户凭证

##### 前端

安全警告 ⚠️

为了方便在前端 js 中提取登录用户的信息，用户登录后将后台返回的用户信息以明文存储在了浏览器的 SQL 中，方便前端在请求与鉴权时做统一数据共享。但这样导致了很大的安全风险，如果用户修改明文存储的属性就可以来躲过前端的鉴权，访问原本没有权限访问的路由。

![image-20190618004827907](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00011.jpg)

猜测正确的方法，大概是后端返回给前端一个加密的用户凭证(token), 每次请求时都带上这个 token 信息，需要后端进行解密才能获取其中的信息，以防止信息被外部更改。

##### 后端

将用户登录后的信息以 HttpSessionId + 固定字符头的方式将用户的登录信息保存在 Redis 中，方便数据的共享和管理。

![Screenshot 2019-06-18 at 12.47.10 AM](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00012.jpg)

SpringBoot 中安装 Redis 插件后，只需配置基础的 Template 即可自动注入 RedisTemplate 类管理 Redis 中的数据，具体方法可参考： https://juejin.im/post/5ad6acb4f265da239e4e9906

#### 根据用户类别产生不同的路由项

用户和管理员的信息都存储在用户表中，通过一个字段来区分两者的权限。为两个不同角色需要生成不同的路由，方法示例如下

动态路由设置

```javascript
const routes = {
  path: "/order",
  name: "Order",
  component: {
    template: "<router-view></router-view>",
  },
  meta: {
    hasMulSub: true,
    hidden: false,
    icon: "shopping_cart",
  },
  children: [
    {
      path: "manage",
      name: "订单管理",
      component: () => import("@/views/ui-components/VOrderManage.vue"),
      meta: {
        auth: ["admin"], //仅给 admin 加载
      },
    },
  ],
};
```

前端需要区分用户(user)和管理员(admin)，为两种角色加载不同的路由:

```javascript
getFilterRouteChild: function(route) {
      let i = route.children.length;
      while (i--) {
        if (
          route.children[i].meta.auth &&
          !route.children[i].meta.auth.includes(
            JSON.parse(localStorage.getItem("LOGIN_USER")).thirdPartyId
          )
        ) {
          route.children.splice(i, 1); //删除无权限的路由项
        }
      }
      // console.log(route.children);
      return route.children;
    }
```

#### 前后端数据交互

前后端交互的流程，以 **商品概览页** 为例:

后端接口定义

```java
//商品详情页浏览
@RequestMapping(value = "/get", method = {RequestMethod.GET})
@ResponseBody
public CommonReturnType getItem(@RequestParam(name = "id", required = false) Integer id) {
    ItemModel itemModel = itemService.getItemById(id);

    // model -> viewObject
    ItemVO itemVO = convertVOFromModel(itemModel);

    return CommonReturnType.create(itemVO);
}
```

前端使用 axios 进行异步请求后端定义好的接口

```javascript
<script>
...
  // 调用获取商品列表接口
  Vue.prototype.$http
    .get("http://localhost:8088/item/list")
    .then(response => {
    if (response.data.status == "success") {
      this.message = "获取商品列表成功";
      this.items = response.data.data;	// 获取响应数据
    } else {
      this.message =
        "获取商品列表失败，原因为" + response.data.data.errMsg;
    }
  })
    .catch(error => {
    Snackbar.error(error);
  });
...
</script>
```

后端响应成功返回格式示例：

```json
{
  "status": "success", //操作状态
  "data": {
    //响应数据
    "id": 18,
    "title": "Apple iPad Pro",
    "price": 6280,
    "stock": 20,
    "description": "Apple iPad Pro (11-inch, Wi-Fi, 256GB) - Space Gray (Latest Model)",
    "sales": 20,
    "imgUrl": "https://images-na.ssl-images-amazon.com/images/I/61yaUxH6XsL._SL1500_.jpg",
    "promoStatus": 0,
    "promoPrice": null,
    "promoId": null,
    "startDate": null,
    "endDate": null
  }
}
```

### 问题与不足

项目的实现相对比较简单，遗留下未解决的几个大问题：

1. 由于没有学习懂原项目中对的 vuex 全局管理状态及 axios 拦截器的使用，我没有对用户的路由访问做鉴权，只在动态路由生成侧边栏的操作项时根据用户类别做了分类显示，为了弥补这一缺陷，仅在后端增加了更多对操作用户的鉴权，但各个页面都可以通过 url 来访问，这是很不安全与完善的。

2. 在用户调用登陆接口登陆成功后，将用户的登录信息及权限存在 web 浏览器的 localStorage 中已到达全局共享的目的，并对用户的权限进行判断。比如在用户发出订单后调用 localStrage 获取用户的 userId, 以及获取用户的权限以渲染不同的侧边栏路由项。但由于 localStorage 可以手动修改，用户可以通过修改 role(角色) 属性来更改自己的权限，因此也存在很大的安全隐患。和同学讨论后，了解到可以将用户凭证存在 请求头 (header), 后端解析请求头来获取用户凭证和共享信息。未来计划这样更改。

3. 前端未做好充分的对输入正则匹配，后端也未做完整的校验，这样无法避免会产生 SQL 注入与恶意脚本执行等风险，安全性不足。(永远不要相信用户输入)

### 体会

在这个项目中充分学习基础的 vue 模版的使用，对 vue 的数据绑定和模版式渲染的强大有了更深的体会，以前只学习过使用 express 后端 渲染 ejs 这类前后端不分离的项目，使用 vue 后深刻了解到了前后端分离开发的必要和方便强大之处，以及对如何更改整合一个有基础框架的 vue 项目有了一定的经验。

SpringBoot 的配置和拓展让我体验到了框架的强大与简洁，类与方法封装的必要性，体验到了 Java 语言语法严格逻辑清晰的优点，以及短期快速开发一个项目原型的可能性，其中涉及到的稍深的一些原理没有进一步涉及，但对 Spring 的处理逻辑有了进一步的了解。对项目服务器部署和 ngix 做反向代理及负载均衡、Redis 的分布式部署等等都没有进一步了解。需要继续努力。

### 待完成

**1. 使用 vuex 保存用户登陆凭证(token)，并做组件数据的统一管理，对路由请求进行拦截。**

**2. 将 axios 异步请求的方法封装为 API，方便并规范化与后端调用的接口的调用与处理**

### 项目构建

### 前端

#### 下载项目

```bash
git clone https://github.com/AbyssLink/vue-admin-vuetify
cd vue-admin-vuetify
```

#### 安装依赖

```bash
npm install
```

#### 以开发模式(热加载)启动

```bash
npm run serve
```

打开 http://localhost:3000 查看 demo

如果热加载失败
更改 `vue.config.js`

```javascript
module.exports = {
  chainWebpack: (config) => {
    config.resolve.symlinks(true);
  },
};
```

#### 以生产模式启动

```bash
npm run build
```

#### 提示和修复文件

```bash
npm run lint
```

### 后端

#### 下载项目

```bash
git clone https://github.com/AbyssLink/spikeproject.git
```

#### 数据库配置

```bash
# 执行 spikeproject/src/main/resources/sqlscript 下的任意一个 SQL 脚本，创建 MySQL 表结构
```

系统需要预先配置好 Mysql 和 Redis，并适当修改配置

#### 打包项目

```xml
<!-- 在 pom.xml 中配置项目名称 -->
<build>
  <finalName>spike</finalName>
  <plugins>
    <plugin>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-maven-plugin</artifactId>
    </plugin>
  </plugins>
</build>
```

**在 ide 中打开**

```bash
# clean 项目：选中按项目执行 run as maven clean
# 打包项目：选中项目run as maven install
# 执行第三步控制台输出success后，在本地项目根目录的target目录下就有spike.jar
```

#### 启动项目

```bash
java jar spike.jar
```

### Git log

后端
![Screenshot 2019-06-17 at 10.13.49 PM](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00013.jpg)

前端
![Screenshot 2019-06-17 at 10.13.49 PM](https://raw.githubusercontent.com/AbyssLink/pic/master/custom/online_mall_00014.jpg)
