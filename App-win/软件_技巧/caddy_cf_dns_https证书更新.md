#caddy_cf_dns_https证书更新#

---

Caddy 默认通过 Let’s Encrypt 获得 TLS 证书[1]， 90 天有效期，并且会在上一次顺利申请证书 60 天后尝试更新。但是如果我们套上 CDN ，域名指向 CDN 提供的 CNAME，就不能通过默认方法申请 TLS 证书了。

需要 Caddy 有一个额外的模块， dns.providers.cloudflare。可以下载官方编译的，也可以用 xcaddy 编译。





#caddy-源代码 V1
https://github.com/caddyserver/caddy/releases/tag/v1.0.5

---

# go1.14

build xcaddy 自动编译软件

    go install github.com/caddyserver/xcaddy/cmd/xcaddy@latest

build caddy

    xcaddy build --with github.com/caddy-dns/cloudflare

 

#查看caddy插件#

    
    caddy -plugins

caddy v1 xcaddy编译失败，goroot根目录搜索不到模块
v2 编译正常




## 秋水版1.0.5集成了forwardproxy   ##
https://dl.lamp.sh/files/caddy_linux_amd64

自定义模块的编译 https://github.com/shuxs/caddy


---

## caddy v2 ##

xcaddy build 自动编译软件


    xcaddy build v2.6.4 \
	    --with github.com/abiosoft/caddy-exec \
	    --with github.com/imgk/caddy-trojan  \
	    --with github.com/mholt/caddy-webdav \
	    --with github.com/caddy-dns/cloudflare
    
## 编辑-配置文件 ##
    nano /etc/caddy/Caddyfile
    

添加到环境变量中
    export PATH=$PATH:/opt
    

 激活环境变量
      source /etc/profile
    
    
#查看模块
    cd /usr/local/bin
    
    caddy list-modules | grep dns


#测试
    caddy run -config Caddyfile.conf

##测试通过后，让Caddy在后台运行
    caddy start -config Caddyfile.conf
    

## v2中文文档 ##
https://caddy2.dengxiaolong.com/docs/build


#兼容 Caddyfile 运行
    caddy adapt --config Caddyfile
    
### cf网站-配置文件 ###

    cflj=/etc/caddy/Caddyfile
    echo $cflj
    
    ./caddy adapt --config $cflj --validate
    
    ./caddy adapt --config Caddyfile --validate

    ./caddy adapt --config Caddyfile

    ./caddy run adapt --config Caddyfile
	
	caddy run --config $cflj
	
	caddy run --config /path/to/Caddyfile


	cd /root/app/caddy_v2/

    nano $cflj

	#caddy v2 path

    cdv2=/root/app/caddy_v2
    echo $cdv2
	
	cd $cdv2
    ls -l

---
配置文件-格式化

fmt

[https://caddyserver.com/docs/command-line#caddy-fmt](https://caddyserver.com/docs/command-line#caddy-fmt)

./caddy fmt ./Caddyfile

./caddy help fmt

caddy fmt [--overwrite] [--diff] [<path>]




---

## v2 caddyfile ##

    nano Caddyfile
    
- Caddyfile概念

[https://caddy2.dengxiaolong.com/docs/caddyfile/concepts](https://caddy2.dengxiaolong.com/docs/caddyfile/concepts)

- Caddyfile-入门教程

[https://caddy2.dengxiaolong.com/docs/caddyfile-tutorial](https://caddy2.dengxiaolong.com/docs/caddyfile-tutorial)


- caddy 命令行

[https://caddy2.dengxiaolong.com/docs/command-line](https://caddy2.dengxiaolong.com/docs/command-line)


- cf-dns-caddy

[https://cutenico.best/posts/blogs/caddy2-compile-cloudflare-dns/](https://cutenico.best/posts/blogs/caddy2-compile-cloudflare-dns/)

----------

### 查看状态 ###

sudo service caddy status

### 停止程序 ###

sudo service caddy stop


### 启动程序 ###

sudo service caddy start

----------

    caddy run 
	#在前台启动 Caddy 进程
    
	caddy start 
	#在后台启动 Caddy 进程
    
	caddy stop 
	#停止正在运行的 Caddy 进程



将加载并提供适配了的配置以检查有效性（但它实际上不会开始运行配置）。

Examples:
  $ caddy run
  $ caddy run --config caddy.json
  $ caddy reload --config caddy.json
  $ caddy stop



Available Commands:
  adapt          Adapts a configuration to Caddy's native JSON
  add-package    Adds Caddy packages (EXPERIMENTAL)
  build-info     Prints information about this build
  completion     Generate completion script
  environ        Prints the environment
  file-server    Spins up a production-ready file server
  fmt            Formats a Caddyfile
  hash-password  Hashes a password and writes base64
  help           Help about any command
  list-modules   Lists the installed Caddy modules
  manpage        Generates the manual pages for Caddy commands
  reload         Changes the config of the running Caddy instance
  remove-package Removes Caddy packages (EXPERIMENTAL)
  respond        Simple, hard-coded HTTP responses for development and testing
  reverse-proxy  A quick and production-ready reverse proxy
  run            Starts the Caddy process and blocks indefinitely
  start          Starts the Caddy process in the background and then returns
  stop           Gracefully stops a started Caddy process
  trust          Installs a CA certificate into local trust stores
  untrust        Untrusts a locally-trusted CA certificate
  upgrade        Upgrade Caddy (EXPERIMENTAL)
  validate       Tests whether a configuration file is valid
  version        Prints the version

