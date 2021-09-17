#! /bin/bash 

time2="ph$(date "+%Y%m%d%H%M%S").zip"

cd /var/www/dl/wj/yt
zip  -r -0  -P 741852  $time2  phvideo

rclone move   /var/www/dl/wj/yt/$time2   onedrive:/video/phvideo

rm -f /var/www/dl/wj/yt/phvideo/*.mp4
