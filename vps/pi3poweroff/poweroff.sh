#! /bin/bash 

#非www-data  写入权限
# sudo chmod o+w /var/www/poweroff/poweroff.txt

ml1=$(cat /var/www/poweroff/poweroff.txt)


#txt 是否 有 poweroff

if [ ${ml1} == "poweroff" ];
then

#清空 txt
>/var/www/poweroff/poweroff.txt
#关机
bash /home/pi/sh/gj.sh

# 测试 命令
#echo "you poweroff"
#touch /var/www/poweroff/offfile

fi 
