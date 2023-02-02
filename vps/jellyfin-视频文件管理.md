
## jellyfin 视频文件管理 软件 ##

英文安装-帮助

[https://jellyfin.org/docs/general/installation/linux/](https://jellyfin.org/docs/general/installation/linux/)

## 启动sh ##
    sudo nano jellyfin.sh
    

----------

    #!/bin/bash
    JELLYFINDIR="/opt/jellyfin"
    FFMPEGDIR="/usr/share/jellyfin-ffmpeg"
    
    $JELLYFINDIR/jellyfin/jellyfin \
     -d $JELLYFINDIR/data \
     -C $JELLYFINDIR/cache \
     -c $JELLYFINDIR/config \
     -l $JELLYFINDIR/log \
     --ffmpeg $FFMPEGDIR/ffmpeg

### sh 权限设置 ###
    sudo chown -R user:group *
    sudo chmod u+x jellyfin.sh

## 服务文件 ##

    cd /etc/systemd/system
    sudo nano jellyfin.service

----------

    [Unit]
    Description=Jellyfin
    After=network.target
    
    [Service]
    Type=simple
    User=youruser
    Restart=always
    ExecStart=/opt/jellyfin/jellyfin.sh
    
    [Install]
    WantedBy=multi-user.target

### 启动服务 ###

    sudo chmod 644 jellyfin.service
    sudo systemctl daemon-reload

	# power on start
    sudo systemctl enable jellyfin.service
    sudo systemctl start jellyfin.service

	# stop
	sudo systemctl disable jellyfin.service