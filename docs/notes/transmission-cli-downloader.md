# VPS 安装 Transmission 实现离线下载

-- 此文仅做留存，相比 Transmission 可以使用更方便的 [CCAA](https://github.com/helloxz/ccaa) --

由于 ✈️ 场命令禁止 PT 和 BT，和群友交流后明白了用 VPS 做中转下载 BT，下载完成再 Pull 到本地。

## Install Transmission-daemon

```bash
sudo add-apt-repository ppa:transmissionbt/ppa
sudo apt-get update
sudo apt-get install transmission-daemon
```

## Configuration

transmission-daemon 的配置文件在 `/etc/transmission-daemon/settings.json`

注意修改配置文件时要先把 transmission 停止，不然会被覆写，修改完以后重新启动才会生效

```bash
systemctl stop transmission-daemon
vi /etc/transmission-daemon/settings.json
systemctl start transmission-daemon
```

修改以下内容 ：

- `rpc-authentication-required`: true
- `download-dir`: /var/downloads: 下载的路径
- `rpc-password`: \*\*\*: web 接口的密码，使用纯文本密码替换，再次加载的时候会被进行哈希处理
- `rpc-username`: transmission: web 接口的账户名
- `rpc-whitelist`: 127.0.0.1: 白名单，设成\*表示任何 IP 都可以通过 RPC 协议访问这个 daemon
- `rpc-host-whitelist`: 8.8.8.8,1.1.1.1,8.8.4.4,208.67.222.222,114.114.114.114: dns 服务器，若不添加 Web UI 容易弹出 "connection failed" 的[警告](https://github.com/transmission/transmission/issues/476#issuecomment-379410324)。(FIXME: 配置 dns 后偶尔还是会遇到连接失败的警报)

附：[详细配置文档](https://github.com/transmission/transmission/wiki/Editing-Configuration-Files)

## Use in Web UI

确保 Transmission 在运行，浏览器访问 http://ip-address-of-server:9091

port 可在 settings.json 更改，默认 9091，界面如下：

![](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdereenigne.org%2Fwp-content%2Fuploads%2Ftransmissionwebinterface.png&f=1&nofb=1)

然后就可以开始愉快地下载 BT 和 PT 文件了，下载完成后再从远程 pull 到本地，或者在远程安装 File Manager 查看。

## Custom web UI

参考: [transmission-web-control](https://github.com/ronggang/transmission-web-control)
