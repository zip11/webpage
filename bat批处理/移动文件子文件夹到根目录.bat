::@echo off
set yue="8"
echo %yue%

set pan="I:\xz t\"
echo %pan%

set /p "DstFolder=dest dir:"
for /f "delims=" %%i in ('dir /a-d /s /b *.mp4') do (
    move "%%i" "I:\xz t\%yue%-%DstFolder%-2020"
)
for /f "delims=" %%i in ('dir /a-d /s /b *.mkv') do (
    move "%%i" "I:\xz t\%yue%-%DstFolder%-2020"
)
del UUE29.mp4
echo "ok"
pause