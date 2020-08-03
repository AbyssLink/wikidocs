# 一个简易的图书推荐系统

## Code

Front-end: https://github.com/AbyssLink/vue-admin-vuetify/tree/Book-Recommend-Flask-backend

Back-end: https://github.com/AbyssLink/book-recommendation-system

### ScreenShots

| 图书首页                                                                                                   | 模糊搜索                                                                                                   |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| ![Screen Shot 2019-07-15 at 1.27.19 AM](https://ww3.sinaimg.cn/large/006tNc79ly1g50c7pdxstj31bf0u0x1e.jpg) | ![Screen Shot 2019-07-15 at 1.28.33 AM](https://ww4.sinaimg.cn/large/006tNc79ly1g50c7rsln4j31bf0u0wrt.jpg) |
| 图书评分                                                                                                   | 图书推荐                                                                                                   |
| ![Screen Shot 2019-07-15 at 1.27.39 AM](https://ww3.sinaimg.cn/large/006tNc79ly1g50c7s9se7j31bf0u0wnf.jpg) | ![Screen Shot 2019-07-15 at 1.37.28 AM](https://ww2.sinaimg.cn/large/006tNc79ly1g50c7tabfxj31bf0u01kx.jpg) |
| 个人信息                                                                                                   |                                                                                                            |
| ![Screen Shot 2019-07-15 at 1.37.46 AM](https://ww3.sinaimg.cn/large/006tNc79ly1g50c7tjx7hj31bf0u00z8.jpg) |                                                                                                            |

## QuickStart

### 前端

#### 下载项目

```shell
git clone https://github.com/AbyssLink/vue-admin-vuetify.git
# 切换分支
git checkout Book-Recommend-Flask-backend
cd vue-admin-vuetify
```

#### 安装依赖

```shell
npm install
```

#### 以开发模式(热加载)启动

```shell
npm run serve
```

#### 以生产模式启动

```shell
npm run build
```

### 后端

#### 下载项目

```shell
git clone https://github.com/AbyssLink/Book_Recommend_System.git
cd  Book_Recommend_System
```

#### 配置依赖

```shell
pipenv install
# or
pip install -r requirements
```

#### 运行 Flask

```shell
python app.py
```

## 实验内容

### 需求

实现一个简单的图书推荐系统，可以在已有的数据源上对用户进行简单的图书推荐。

支持用户实时添加评分，并更新推荐结果。

### 详细设计

项目的前端总体实现比较简单，由于 vuetify 本身就是已经非常成熟的响应式框架，我在样式和布局上主要通过修改一些组件的预设完成，主要的工作量在于前后端跨域请求数据和前端的用户状态管理问题。

#### 技术栈

```
Vue + Vuetify + Flask + SQLAlchemy + mysql
```

#### 开发工具

操作系统：`MacOS 10.14.15`

前端 IDE：`Visual Studio Code`

后端 IDE: `Pycharm`

数据库：`Mysql 8.0.15`, `redis 5.0.5`

#### 前端依赖库

1. 组件样式: `vuetify`, `material-design-icons-iconfont`
2. 路由处理: `vue-router`
3. ajax 请求: `axios`
4. 时间处理: `moment`

#### 后端依赖库

1. Web 框架：`Flask`
2. 处理跨域请求：`flask_cors`
3. 数据库 ORM 框架：`Flask-SQLAlchemy`
4. 数据处理：`Pandas`, `Numpy`, `math`, `operator`

#### 数据库表结构

使用了 MySQL 数据库，主要为 Book，User，Rating 表，Book 表为图书基本信息，User 表为用户基本信息，Rating 表为用户对特定图书的评分。

##### ER 图：

| Navicat 生成                                                                                                                         | DBViewer 生成                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| ![Screen Shot 2019-07-15 at 10.26.22 AM](https://raw.githubusercontent.com/AbyssLink/pic/master/book-recommend-system-2019-07_1.jpg) | ![Screen Shot 2019-07-15 at 10.26.05 AM](https://raw.githubusercontent.com/AbyssLink/pic/master/book-recommend-system-2019-07_5.jpg) |

数据源：http://www2.informatik.uni-freiburg.de/~cziegler/BX/

使用的数据源来自网络上开源 2004 年的图书数据库，下载的原始文件为 CSV 格式。

处理的数据量较大，Book 表和 User 表的数据约为 30 万行。

### 推荐系统实现

#### 数据预处理

使用 Python 的 Pandas 库，对 CSV 文件进行了行遍历，过滤了一些字段中编码非 utf-8 与数据列数目不正确的列，再使用 Navicat 的 Import Wizard 工具将 CSV 文件导入为 MySQL 表格。

#### 用户登陆

前台向后台发送登陆表单的信息，同时接受后台发送的用户详细信息存储在浏览器本地缓存(localStorage), 以在前端显示用户头像，用户名等.

```javascript
login() {
      Vue.prototype.$http
        .post("/login", this.userInfo)
        .then(response => {
          if (response.data.status == "success") {
            // 存储登陆信息在客户端浏览器中
            let userFullInfo = response.data.data;
            localStorage.setItem("LOGIN_USER", JSON.stringify(userFullInfo));
            this.message = "登陆成功";
            Snackbar.success(this.message);
      			// 登陆成功后跳转页面
            this.$router.push({ name: "Index" });
          } else {
            this.message = "登陆失败，原因为" + response.data.errMsg;
            Snackbar.error(this.message);
          }
        })
        .catch(error => {
          console.log(error);
          Snackbar.error(error);
        });
    }
```

后台接受前台 post 的表单数据，与后台 User 表进行验证，并返回对应状态码给前台：

```python
@app.route('/login', methods=['POST'])
def login():
    response = {}
    user_id = request.form['userId']
    password = request.form['password']
    login_user = User.query.filter_by(id=user_id).first()
    if login_user is not None:
        if login_user.password == password:
            response['status'] = 'success'
            response['data'] = User.as_dict(login_user)
            return json.dumps(response)
        else:
            response['status'] = 'fail'
            response['errMsg'] = '密码不正确'
            return json.dumps(response)
    else:
        response['status'] = 'fail'
        response['errMsg'] = '用户名不存在'
        return json.dumps(response)
```

#### 添加评价

前端以表单形式添加一条评价记录，后端通过获取参数使用数据库方法查询是否已有评分记录，已有则更新评分，否则新建评分。

前台使用 post 方法发送表单数据：

```javascript
// 发送用户评分请求
addRate() {
      this.dialog = false;
      this.form.userId = this.userId;
      this.form.bookId = this.item.item_id;
      this.form.score = this.rating * 2; // 0～5分制 => 0~10分制
      console.log(this.form);
      Vue.prototype.$http
        .post("/rating/add", this.form)
        .then(response => {
          if (response.data.status == "success") {
            this.message = "评价成功";
           ...
          } else {
            ...
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
```

设置后台响应：

```python
# 添加用户评分
@app.route('/rating/add', methods=['POST'])
def add_rate():
    user_id = request.form['userId']
    book_id = request.form['bookId']
    score = request.form['score']
    rating = Rating.query.filter_by(user_id=user_id, book_id=book_id).first()
    if rating is not None:
        rating.score = score
    else:
        db.session.add(Rating(user_id=user_id, book_id=book_id, score=score))
    db.session.commit()
    response = {'status': 'success'}
    return json.dumps(response)
```

#### 基于协同过滤推荐

```python
# 基于物品相似度的协同过滤推荐公式：
similar[i][j] = u(i) ∩ u(j) / sqrt(u(i) * u(j))
predict[u][j] = ∑( i ∊ n(u) ∩ similar(j, k) ) similar[i][j] * rate[u][i]
```

算法的主要的步骤是计算相似度然后根据相似度排序，对用户的行为进行遍历，形成推荐列表。

**相似度中贡献度的计算函数：**

```python
def update_contribute_score(user_total_rate_num):
    """
    item cf update sim contribution score by user
    点击数目越少，贡献度越高，数目越多贡献度越低
    """
    return 1 / math.log10(1 + user_total_rate_num)
```

**计算相似度（以基于物品推荐为例）：**

```python
# itemcf.py
def cal_item_sim(user_like):
    # 评价 item 的公共用户
    co_appear = {}
    # 评价 item 的所有用户
    item_user_like_count = {}
    for user, item_list in user_like.items():
        for i in range(0, len(item_list)):
            ....
            for j in range(i + 1, len(item_list)):
                item_id_j = item_list[j]
                co_appear.setdefault(item_id_i, {})
                co_appear[item_id_i].setdefault(item_id_j, 0)
                # 存储 item_i 对 item_j 的贡献
                co_appear[item_id_i][item_id_j] += update_contribute_score(
                    len(item_list))
                co_appear.setdefault(item_id_j, {})
                co_appear[item_id_j].setdefault(item_id_i, 0)
                # 存储 item_j 对 item_i 的贡献
                co_appear[item_id_j][item_id_i] += update_contribute_score(
                    len(item_list))
    	...
    	#  排序实现
      return item_sim_score_sorted
```

#### 模糊搜索

使用数据库中间件封装完成的方法对数据库中的所有字段进行遍历，相似的行转化为为列表输出。

```python
# 根据字段查询书籍
@app.route('/book/search/<content>')
def search_book(content):
    rows = Book.query.filter(
        or_(Book.id.like("%" + content + "%") if content is not None else "",
            Book.title.like("%" + content + "%") if content is not None else "",
            Book.author.like("%" + content + "%") if content is not None else "",
            Book.publisher.like("%" + content + "%") if content is not None else "",
            Book.year.like("%" + content + "%") if content is not None else "")
    ).limit(100)

    response = {}
		...

    return json.dumps(response)
```
