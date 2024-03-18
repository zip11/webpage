@echo off

REM 输入视频文件路径
set /p input_file=请输入视频文件路径: 

REM 获取视频信息
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate -of default=noprint_wrappers=1:nokey=1 "%input_file%"

pause
