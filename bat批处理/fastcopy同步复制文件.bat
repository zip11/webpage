@echo off
set yue="7"
echo %yue%

set /p "copyfl=input source folder"

"c:\FastCopy341_x64\FastCopy.exe" /cmd=diff "Q:\u\%yue%-%copyfl%" /to="E:\e\%yue%-%copyfl%" 