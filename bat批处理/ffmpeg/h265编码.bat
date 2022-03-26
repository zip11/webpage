::全部时间120second  开始时间 110second
cd /d %~dp0
set mz="*.mp4"
ffmpeg -ss 110 ^
-i %mz%   ^
-c:v libx265 -vf scale=1920:1080 -preset ultrafast -x265-params  ^
crf=22:qcomp=0.8:aq-mode=1:aq_strength=1.0:qg-size=16:psy-rd=0.7:psy-rdoq=5.0:rdoq-level=1:merange=44 ^
-c:a copy ^
-t 120 

pause