#!/bin/bash 
#lcd1602 
echo "lcd1602_display "
select var in  "启动" "关闭lcd1602" "重启" "开机启动" "禁止开机启动";do

#输入数字，选择选项
    break

done

echo "已经选择$var"

case $var in

#匹配选择
    "启动") sudo systemctl start lcd1602;;
    "关闭lcd1602") sudo systemctl stop lcd1602;;
    "重启") sudo systemctl restart lcd1602;;
    "开机启动" ) sudo systemctl enable lcd1602;;
    "禁止开机启动" ) sudo systemctl disable lcd1602;;
    # sudo systemctl daemon-reload;

esac 
