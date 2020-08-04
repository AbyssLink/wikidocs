# 一个简单的 Yande.re 爬虫

Yande.re 提供了详尽方便的 API，于是写了个用 API 下载 yande.re 图片的 Python 脚本

## Code

[yande-crawler](https://github.com/AbyssLink/yande-crawler)

## Usage

```
git clone https://github.com/AbyssLink/yande-downloader.git

cd yande-crawler

pip install -r requirements.txt

python3 client.py
# example input argument
Search Tags = yuri
Start Page = 10
End Page = 15
Download Path = ''
# if path dosen't exist, will use default path = <project_path>/download
```

## API

Using [API](https://yande.re/help/api) from yande.re.

## Reference

Code structure referenced to [konadl](https://github.com/k4yt3x/konadl)

## ScreenShots

![](https://raw.githubusercontent.com/AbyssLink/pic/master/yande-crawler_screenshots_1.png)

![](https://raw.githubusercontent.com/AbyssLink/pic/master/yande-crawler_screenshots_2.png)
