dim lj1,lj2,lj3,lj4
Public Const vbQuote = """"
lj1 = "C:\Program Files\Sandboxie-Plus\Start.exe"
lj2 = " /box:DefaultBox "
lj3 = "Z:\app\game\Amnesia-version_0.90a-pc\Amnesia.exe"
lj4 = vbQuote &   lj1  & lj2 & vbQuote
MsgBox(lj4)
'  "" Z:\app\game\Amnesia-version_0.90a-pc\Amnesia.exe""
Set WshShell = WScript.CreateObject("WScript.Shell")
strDesktop = WshShell.SpecialFolders("Desktop") :'�����ļ��С����桱
set oShellLink = WshShell.CreateShortcut(strDesktop & "\sb.lnk")
oShellLink.TargetPath = lj4 : 'Ŀ��
oShellLink.WindowStyle = 1 :'����1Ĭ�ϴ��ڼ������3��󻯼������7��С��
oShellLink.Hotkey = "" : '��ݼ�
oShellLink.IconLocation = lj3 : 'ͼ��
oShellLink.Description = "sb" : '��ע
oShellLink.WorkingDirectory = "" : '��ʼλ��
oShellLink.Save : '���������ݷ�ʽ
MsgBox("ink make ok")