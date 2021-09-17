#! /bin/bash

#mei you part move *.mp4

lj1="/var/www/dl/wj/yt/video"

cd $lj1

if [ -e *.mp4 ]
then
   echo 'part cun zai'
else
   echo 'mp4 mei you'
   exit
fi

cd $lj1

#mei you part move *.mp4
if [ -e *.part ]
then

   echo 'part cun zai'

else

   echo 'part mei you'
   rclone move   $lj1  onedrive:/video

fi


