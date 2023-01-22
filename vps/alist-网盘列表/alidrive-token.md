## 阿里云盘 ##

手机安装mt文件管理器，有root权限

refresh_token（刷新令盘）：如何获取参考这个issue 通过手机端抓包 / 查找日志（/data/media/0/Android/data/com.alicloud.databox/files/logs/trace/你的网盘useid/yunpan）来获取, 

上面的“你的网盘userid”一般就是一串数字，如果你登录过多个网盘账号，trace这个文件夹内就会有多个网盘ID

最终在对应网盘的yunpan文件夹里面，会看到很多log结尾的文件，这就是登录的日志文件

点击查看最新日期的log日志文件，如果你手机内有代码编辑器最好了，没有的话，随便用什么文档查看，然后在里面查找 refreshToken


----------

### 文件夹id ###

或使用 https://media.cooluc.com/decode_token/
根目录 file_id：打开阿里云盘官网，点进去你要设置的文件夹时 url 后面的一串，如 https://www.aliyundrive.com/drive/folder/5fe01e1830601baf774e4827a9fb8fb2b5bf7940 就是 5fe01e1830601baf774e4827a9fb8fb2b5bf7940


order_by（排序）：可选值为name，size，updated_at，created_at
order_direction（排序方向）：可选ASC（正序），DESC（倒序）