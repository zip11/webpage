# alist 网页 网盘文件列表 程序 #

帮助文档

[https://alist.nn.ci/zh/guide/install/manual.html](https://alist.nn.ci/zh/guide/install/manual.html)

## 手动安装 ##

    # 解压下载的文件，得到可执行文件：
    tar -zxvf alist-xxxx.tar.gz
    
    # 授予程序执行权限：
    chmod +x alist
    
    # 运行程序
    ./alist server
    
    # 获得管理员信息
    ./alist admin
    

### 静默后台启动 ###

    # 携带`--force-bin-dir`参数启动服务
    alist start

    # 通过pid停止服务
    alist stop

    # 通过pid重启服务
    alist restart

## 守护进程 ##

使用任意方式编辑 

sudo nano /usr/lib/systemd/system/alist.service 

并添加如下内容，其中 path_alist 为 AList 所在的路径

    [Unit]
    Description=alist
    After=network.target
     
    [Service]
    User=pi
    Group=pi
    Type=simple
    WorkingDirectory=path_alist
    ExecStart=path_alist/alist server
    Restart=on-failure
     
    [Install]
    WantedBy=multi-user.target


然后，执行  sudo systemctl daemon-reload 重载配置，现在你可以使用这些命令来管理程序：

    启动: 
	sudo systemctl start alist

    关闭: 
	systemctl stop alist

    配置开机自启: 
	sudo  systemctl enable alist

    取消开机自启: 
	systemctl disable alist

    状态: 
	systemctl status alist

    重启: 
	sudo systemctl restart alist


## 添加存储 ##

## 本地存储 ##

挂载路径
唯一标识，即要挂载到的位置，如果要挂载到根目录，就是 /


### 根文件夹路径 ###
您要挂载的文件夹的路径。 例如：

Linux: /root
Windows: C:


## WebDAV 配置 ##

http://domain:port/dav/

dav/ 是软件自带的路径不能删除