# GitHub Pages 同步私密仓库 hexo 博客

最近把 Hexo 博客的 GitHub 仓库变成 private 了，记录一下重新 deploy 的过程。

仓库权限变成 private 以后就不能用 travis-ci.org 的免费自动化集成方案了，于是在本机生成 html。
诶为啥 push 到 GitHub Pages 后变成全空白的了？看了眼 hexo generate 生成的 public html:

```bash
du -sh ./public
  0B    ./public
```

（全空文件，草）

找到 [issues](https://github.com/hexojs/hexo/issues/4289)，是 Hexo 和 nodejs 14 不兼容导致。

想了三个解决方案：

1. 安装 lts 版本的 nodejs
   可以使用 lts 版本的 nodejs 以正常使用 hexo，但 macOS 有好几个 brew package 依赖 stable 版本的 nodejs，放弃
2. 使用 nodejs 版本管理工具 （ n 和 nvm ）
   看了下文档，需更改 /usr/local 文件夹权限，感觉对本机环境的影响比较大，而且 nvm 冷启动会拖慢 zsh 的速度，放弃
3. 使用新环境（虚拟机、VPS）
   可以保证本机环境的纯净，但操作相对繁杂。

想来想去，还是选第三种方案，既然用虚拟机，就用 docker 跑个 ubuntu 来 build 吧...

## docker 运行 ubuntu

```bash
docker info
docker search ubuntu
docker pull ubuntu
docker images
# run ubuntu in iteractive shell
docker run -it ubuntu
# see all containers
docker ps -a
# run ubuntu images after exit
docker exec -it <container id> /bin/bash
```

## push 到 GitHub Pages

编写一个 shell 脚本放在 docker ubuntu 里，每次 source repository 更新后重新生成 html files， push 到 GitHub Pages 仓库。

由于 source repository 为 private，使用有 repository 操控权限的 github presonal access token 来 clone repository。

警告 ⚠️：**该 token 有操控所有 repository 的权限，以明文存储在文件中不安全。** 比如，拥有 token 的对象可以对所有的仓库进行 force push 覆盖原有内容，如果这些仓库的代码没有备份就凉凉了。

目前 token 通过 read 命令由用户输入明文，定期到 https://github.com/settings/tokens 重新生成 token 保障安全性。

```bash
# /usr/bin/bash

# variables
USER_NAME=<YOUR_NAME>
USER_EMAIL=<YOUR_EMAIL>
GH_SOURCE=github.com/$USER_NAME/<YOUR_PRIVATE_SOURCE_REPO>.git
GH_REF=github.com/$USER_NAME/<YOUR_GITHUB_PAPGES_REPO>.git
REPO_PATH=$USER_NAME/<YOUR_PRIVATE_SOURCE_REPO>

# init enviroment
apt update && apt upgrade
apt install git nodejs npm
apt update && apt upgrade
apt install git nodejs npm
npm install -g yarn
npm install -g hexo-cli

# print enviroment version
node -v
npm -v
yarn -v
hexo -v

# remove old repository
rm -rf $REPO_PATH

# input github token use user input
echo -n "Please input Github personal access token:"
read GH_TOKEN
echo -n "Read token success."

# clone private repository using github token
git clone https://$GH_TOKEN@$GH_SOURCE $REPO_PATH
cd $REPO_PATH

# build html files
yarn install
hexo clean && hexo generate

# push html files to github pages repository
cd ./public
git init
git config user.name $USER_NAME
git config user.email $USER_EMAIL
git add .
git commit -m "build hexo files in docker"
git push --force https://$GH_TOKEN@$GH_REF master:master
```

每次 source repository 更新后，启动 docker ubuntu 运行该脚本更新 GitHub Pages。
好，页面终于回来了。

## References

bash tutorial by 阮一峰:

https://wangdoc.com/bash/intro.html

use ubuntu in docker:

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

build hexo with travis-ci:

https://molunerfinn.com/hexo-travisci-https/#编写-travis-yml
