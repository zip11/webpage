@echo off
::���ó�����ļ���·������ѡ��
set Program=D:\Program Files\Microvirt\MEmu\MEmu.exe

::����������������ѡ��
set  Arguments=

::���ÿ�ݷ�ʽ���ƣ���ѡ��
set LnkName=test

::���ó���Ĺ���·����һ��Ϊ������Ŀ¼�����������գ��ű������з���·��
set WorkDir=

::���ÿ�ݷ�ʽ��ʾ��˵������ѡ��
set Desc=

if not defined WorkDir call:GetWorkDir "%Program%"
(echo Set WshShell=CreateObject("WScript.Shell"^)
echo strDesKtop=WshShell.SpecialFolders("DesKtop"^)
echo Set oShellLink=WshShell.CreateShortcut(strDesKtop^&"\%LnkName%.lnk"^)
echo oShellLink.TargetPath="%Program%"
echo oShellLink.Arguments="%Arguments%"
echo oShellLink.WorkingDirectory="%WorkDir%"
echo oShellLink.WindowStyle=1
echo oShellLink.Description="%Desc%"
echo oShellLink.Save)>makelnk.vbs
echo �����ݷ�ʽ�����ɹ���
makelnk.vbs
del /f /q makelnk.vbs
pause
exit
goto :eof
:GetWorkDir
set WorkDir=%~dp1
set WorkDir=%WorkDir:~,-1%
goto :eof