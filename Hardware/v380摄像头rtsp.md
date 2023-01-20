## v380 rtsp视频地址 ##

VLC播放


标清分辨率
rtsp://192.168.1.21/live/ch00_1

高清分辨率
rtsp://192.168.1.21/live/ch00_0

v380 rtsp网址
[https://www.ispyconnect.com/camera/v380](https://www.ispyconnect.com/camera/v380)

[https://www.right.com.cn/forum/thread-5977236-1-1.html](https://www.right.com.cn/forum/thread-5977236-1-1.html)


## 打开rtsp ##


v380厂家固件升级后关闭了rtsp，需要打开

在tf卡根目录下建个ceshi.ini
内容是

[CONST_PARAM]

rtsp=1


手机安装lws3801.1.30,软件连接好摄像头，点击 设置-高级设置-设备Onvif设置，可能需要多次打开设备Onvif设置，才能显示设置成功

现在rtsp已经打开了





黄灯-外接电源灯
红灯- 摄像头启动，后就关闭
蓝灯- 摄像头运行灯

### 检测摄像头 支持 onvif协议 软件 下载 ###

[https://sourceforge.net/projects/onvifdm/](https://sourceforge.net/projects/onvifdm/)

onvif device manager的感觉可以认为是onvif device test tool的简化版，简化的意思一是功能少了一些，二是功能少了同时操作起来更简单明了。更具体使用可参考：https://wenku.baidu.com/view/3cb0bf1a3c1ec5da51e27002.html

第一步，打开onvif device manager，左侧是当前检测到的支持onvif的设备，可点击“Refresh”按钮刷新列表。实际使用发现不管怎么刷新该工具总是很难发现全部设备，此时可使用“Add”按钮手动添加。

第二步，双击自己要检测的设备，如果该设备真支持onvif那么在中部就会呈现支持的onvif操作。当前图中告警是因为用户名密码错误。第三步，如果设备要求用户名密码那就在左上方的name和password框中分别输入摄像头web端的用户名密码，然后点击“Log in”。注意这里不管输什么都会“登录成功”，但真正发包时只有正确的用户名密码才能完成请求，所以一定要输入正确的web端用户名密码。

作者：z7-iReview
链接：https://www.zhihu.com/question/404251421/answer/2623255563
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
