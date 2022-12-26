@echo off

echo "java value write, !!! admin-run-cmd !!!"

:: ~~~1~~~ Java Home -Wr

set JAVA_HOME1="D:\Program Files\Java\jdk1.8.0_333"
echo %JAVA_HOME1%

setx /M JAVA_HOME %JAVA_HOME1%


:: ~~~~2~~~~  ClassPath - wr

set CLASSPATH=".;%%JAVA_HOME%%\lib;%%JAVA_HOME%%\lib\dt.jar;%%JAVA_HOME%%\lib\tools.jar;"
echo %CLASSPATH%

setx /M CLASSPATH %CLASSPATH%


:: ~~~~ 3 st ~~~~~

:: path - add java-bin

set jdkpath="%%JAVA_HOME%%\bin;%%JAVA_HOME%%\jre\bin"

:: read old path
set oldpath=%PATH%

setx /M PATH "%jdkpath%;%oldpath%"

echo "write ok"

pause