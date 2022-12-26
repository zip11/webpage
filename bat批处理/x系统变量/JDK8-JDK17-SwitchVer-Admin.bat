@echo off

echo "jdk8-jdk17 SWITCH ver -JAVA_HOME value write, !!! admin-run-cmd !!!"

:: ~~~1~~~ Java 17 Home -Wr

set JAVA_HOME17="D:\Program Files\Java\jdk-17.0.5"
echo %JAVA_HOME17%

setx /M JAVA_HOME17 %JAVA_HOME17%


:: ~~~~2~~~~  JAVA_HOME8 - wr

set JAVA_HOME8="D:\Program Files\Java\jdk1.8.0_333"
echo %JAVA_HOME8%

setx /M JAVA_HOME8 %JAVA_HOME8%


:: ~~~~ JAVA_HOME SWITCH st ~~~~~

:: JDK VER 17
echo "JDK Set VER 17!!!"
set jdkpath="%%JAVA_HOME17%%"

setx /M JAVA_HOME "%jdkpath%"

:: classpath ,jdk6 after

:: old,classpath
::setx /M CLASSPATH "%%JAVA_HOME%%\lib"

:: delete classpath
REG delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /F /V CLASSPATH

echo "JDK VER SWITCH ok"

pause