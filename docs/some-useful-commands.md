# 个人常用的一些命令


As a command manual tool, instead of `man`, `tldr` is very simple and easy to use, and can list some common usages of commands.

## Linux NetWorkTools

In general, Linux network commands involve so few pieces:

- Network Configuration： ifconfig、 ip
- Connectivity detection： ping、 traceroute、 telnet、 mtr
- Internet connection： netstat、 ss、 nc、 lsof
- Traffic Statistics： ifstat、 sar、 iftop
- Switching and routing： arp、 arping、 vconfig、 route
- Firewall： iptables、 ipset
- DNS： host、 nslookup、 dig、 whois
- Capture： tcpdump
- Virtual device： tunctl、 brctl、 ovs

## NetWork Tools

```bash
# View export ip from command line
http ifconfig.co/json
http myip.ipip.net
```

## Network Proxy

```bash
# check ip
curl cip.cc
http ifconfig.co/json
curl ifconfig.co
curl ipinfo.io

# Set ssh specific ip proxy
Host xx.xx.xx.xx
  HostName xx.xx.xx.xx
  ProxyCommand nc -X 5 -x 127.0.0.1:7891 %h %p
  ServerAliveInterval 30

# set curl proxy
# modify curl configuration file
vim ~/.curlrc
# write this line
socks5 = "127.0.0.1:<prot_number>"

# If the proxy is not needed temporarily use the following parameters
curl --noproxy "*" http://www.google.com
```

## ImageMagick

```bash
# view picture information
identify image.png

# format conversion
convert a.gif a.png

# batch format conversion
for f in *png; do convert "$f" "$f.jpg"; done;

# for Github Pic bed
mogrify -quality 75 -resize 1500x1000 *.jpg

# adjust size, resolution, quality
convert image -resize 1200x1200 -density 72 -quality 75 resultimage

# convert a group of pictures to gif
mogrify -path newdir -format png  *.gif
```

## FFmpeg

```bash
# view video information
ffprobe example.mkv

# format conversion
ffmpeg -i example.mkv -c copy example.mp4

# adjust bit rate
ffmpeg -i input.avi -b:v 1500K output.mp4
ffmpeg -i file.avi -b 1.5M file.mp4

# adjust dimension
ffmpeg -i input.avi -vf scale=1920:-2 output.mp4

# adjust frames
ffmpeg -i input.avi -r 30 output.mp4

# adjust resolution
ffmpeg -i input.jpg -vf scale=1080:-2 out.jpg

# ** Batch Process **
# Unix one-liner example i.e. MacOS/Linux
for f in *.mkv; do ffmpeg -i "$f" -c copy "${f%.mkv}.mp4"; done

# Windows one-liner example
for /R %f IN (*.mkv) DO ffmpeg -i "%f" -c copy "%~nf.mp4"
```

## Files

```bash
# view file encoding
file test.py


# sort and view the current file (folder) size
du -sh * | sort -h


# view file hashes
md5 /path/to/file
shasum -a 1 /path/to/file
shasum -a 256 /path/to/file
shasum -a 512 /path/to/file


# the "Text Editing" application is opened in simplified Chinese by default
defaults write com.apple.TextEdit AppleLanguages '(zh-CN)'
# recover
defaults write com.apple.TextEdit AppleLanguages '(en-US)'
```
