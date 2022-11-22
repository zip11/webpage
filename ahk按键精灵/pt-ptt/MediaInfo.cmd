set /P "ml=input video file"
"D:\app\host\MediaInfo_CLI_22.09_Windows_x64\MediaInfo.exe"  --Output=file://custom.txt   %ml% > %ml%.txt

pause