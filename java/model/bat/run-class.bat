set /p a=������*.class����:

:: del .class file name
java  %a:~0,-6%

pause