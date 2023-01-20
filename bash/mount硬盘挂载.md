1 安装exfat的支持软件
命令：

    sudo apt-get install exfat-fuse

2 重启
命令：

    sudo shutdown -r now


3 插上U盘、移动硬盘

4 查看信息
命令：

    sudo fdisk -l 

---

5 挂载
命令：

    cd /mnt
    sudo mkdir yjk_usb

完成创建挂载的目录。

然后执行命令进行挂载：

    sudo mount /dev/sdb1 /mnt/yjk_usb



6 执行你对该文件的操作

7 卸载
完成操作后需要先执行以下命令卸载U盘、移动硬盘，再将其拔出：

    sudo umount /mnt/yjk_usb