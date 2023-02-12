# 树莓派通过wifi共享有线网络 #





    # git命令下载软件 
    git clone https://github.com/oblique/create_ap.git
    
    # 编译-安装软件
    cd create_ap
    sudo make install
 
  
 
#安装依赖库

    sudo apt-get install util-linux procps hostapd iproute2 iw haveged dnsmasq
 
 
 就这样安装好了


启动无线AP：

sudo create_ap wlan0 eth0 热点名 密码
 
 
桥接互联网共享：

create_ap --no-virt -m bridge wlan0 eth0 MyAccessPoint MyPassPhrase
 
 
### 系统化服务 ###

使用持久性systemd服务
 
    #立即开始服务：
     
    sudo systemctl start create_ap
     
    #关闭进程
    sudo systemctl stop create_ap
     
    开机启动：
    systemctl enable create_ap
 
#修改 服务文件
 sudo nano  /usr/lib/systemd/system/create_ap.service
 
#修改 启动命令
ExecStart=/usr/bin/create_ap --config /etc/create_ap.conf
 
 
卸载
办法也比较简单，当初安装是在对应目录下 make install，卸载就是在当初那个目录里 make uninstall。
 
