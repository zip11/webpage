#!/bin/bash
#"mount 2.5inch 500g Usb"

hddlj="/home/pi"

echo "mount 2.5inch 500g Usb"

select var in  "挂载硬盘500g" "弹出硬盘500g" ;do

#输入数字，选择选项
    break

done

echo "已经选择"


case $var in

#匹配选择
    "挂载硬盘500g" ) sudo mount /dev/sdc2 $hddlj ;;
    "弹出硬盘500g" ) sudo umount $hddlj;;

esac
