# 个人常用命令

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

## deploy and maintain in the server:

- Docker + Terraform
- ansible-playbook
- simple way: write a shell and manage it with systemd

## NetWork Tools

```bash
# View export ip from command line
http ifconfig.co/json
http myip.ipip.net
```

## Download

```bash
# references: https://unix.stackexchange.com/questions/272868/download-only-format-mp4-on-youtube-dl
# download youtube videos use mp4 format and with auto generated subtitle
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' --auto-number --write-auto-sub <url>
# or
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -o "%(playlist_index)s-%(title)s.%(ext)s" --write-auto-sub <url>
# download selected subtitle
youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' -o "%(playlist_index)s-%(title)s.%(ext)s" --write-sub --sub-lang en <url>
# download only subtitles
youtube-dl --write-sub --sub-lang en --skip-download <url>
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

# Batch convert to mp3
# only mp4
mkdir outputs
for f in *.mp4; do ffmpeg -i "$f" -c:a libmp3lame "outputs/${f%.mp4}.mp3"; done

# m4a, mov and flac
mkdir outputs
for f in *.{m4a,mov,flac}; do ffmpeg -i "$f" -c:a libmp3lame "outputs/${f%.*}.mp3"; done
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
