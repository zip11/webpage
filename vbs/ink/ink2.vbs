dim lj4
lj4 = "c:\123.exe"
Set WshShell = WScript.CreateObject("WScript.Shell")
strDesktop = WshShell.SpecialFolders("Desktop") :'�����ļ��С����桱
set oShellLink = WshShell.CreateShortcut(strDesktop & "\sb.lnk")
oShellLink.TargetPath = lj4 : 'Ŀ��
oShellLink.WindowStyle = 1 :'����1Ĭ�ϴ��ڼ������3��󻯼������7��С��
oShellLink.Hotkey = "" : '��ݼ�
oShellLink.IconLocation = lj4 : 'ͼ��
oShellLink.Description = "sb" : '��ע
oShellLink.WorkingDirectory = "" : '��ʼλ��
oShellLink.Save : '���������ݷ�ʽ
MsgBox("ink make ok")