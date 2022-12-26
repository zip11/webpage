@echo off

echo "User Path value write, "

:: ~~~1~~~ Java Home -Wr

set userpath="%%USERPROFILE%%\AppData\Local\Microsoft\WindowsApps;C:\WINDOWS\system32;C:\WINDOWS"

echo %userpath%

setx  Path %userpath%


echo "write ok"

pause