#! /bin/bash 

cd /var/www/dl/wj/yt/video


files=$(ls *.mp4 2> /dev/null | wc -l)

if [ "$files" != "0" ] ;
then
   echo 'mp4 cun zai'
else
   echo 'mp4 mei you'
   exit
fi


#vtt字幕
for files in `ls |grep *.vtt`
do
    # 删除 
    fname=${files/.zh-Hans/.mp4}


    # 拼接成文件名
    filename=$fname

    # 更改文件名
    mv $files $filename
done


#mei you part move *.mp4
files=$(ls *.part 2> /dev/null | wc -l)

if [ "$files" != "0" ] ;
then
   echo 'part cun zai'
else
   echo 'part mei you'
   rclone move   /var/www/dl/wj/yt/video  onedrive:/video
fi




time2="ph$(date "+%Y%m%d%H%M%S").zip"

cd /var/www/dl/wj/yt
zip  -r -0  -P 741852  $time2  phvideo

rclone move   /var/www/dl/wj/yt/$time2   onedrive:/video/phvideo

rm -f /var/www/dl/wj/yt/phvideo/*.mp4

