## 阿里云盘 ##

手机安装mt文件管理器，有root权限

refresh_token（刷新令盘）：如何获取参考这个issue 通过手机端抓包 / 查找日志（/data/media/0/Android/data/com.alicloud.databox/files/logs/trace/你的网盘useid/yunpan）来获取, 

上面的“你的网盘userid”一般就是一串数字，如果你登录过多个网盘账号，trace这个文件夹内就会有多个网盘ID

最终在对应网盘的yunpan文件夹里面，会看到很多log结尾的文件，这就是登录的日志文件

点击查看最新日期的log日志文件，如果你手机内有代码编辑器最好了，没有的话，随便用什么文档查看，然后在里面查找 refreshToken


### 手机版 网页 登录 获取 token ###
[https://media.cooluc.com/decode_token/](https://media.cooluc.com/decode_token/)

### 电脑获取token ###

准备事项
一、首先要有一个属于自己的阿里云盘账号（一般为手机号）；

二、在电脑上打开浏览器，进入阿里云盘的官网地址，输入阿里云盘账号和密码登陆；

三、在浏览器上按一次 F12 键，进入开发者工具模式，在顶上菜单栏点 Application ，然后在左边菜单找到 Local storage 下面的 https://www.aliyundrive.com 这个域名，点到这个域名会看到有一个 token 选项，再点 token ，就找到 refresh_token 了，如下图所示

----------

### 文件夹id ###

或使用 https://media.cooluc.com/decode_token/
根目录 file_id：打开阿里云盘官网，点进去你要设置的文件夹时 url 后面的一串，如 https://www.aliyundrive.com/drive/folder/5fe01e1830601baf774e4827a9fb8fb2b5bf7940 就是 5fe01e1830601baf774e4827a9fb8fb2b5bf7940


order_by（排序）：可选值为name，size，updated_at，created_at
order_direction（排序方向）：可选ASC（正序），DESC（倒序）