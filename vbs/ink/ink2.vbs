dim lj1,lj2,lj3,lj4
Public Const vbQuote = """"
lj1 = "C:\Program Files\Sandboxie-Plus\Start.exe"
lj2 = " /box:DefaultBox "
lj3 = "Z:\app\game\Amnesia-version_0.90a-pc\Amnesia.exe"
lj4 = vbQuote &   lj1  & lj2 & vbQuote
MsgBox(lj4)
'  "" Z:\app\game\Amnesia-version_0.90a-pc\Amnesia.exe""
Set WshShell = WScript.CreateObject("WScript.Shell")
strDesktop = WshShell.SpecialFolders("Desktop") :'特殊文件夹“桌面”
set oShellLink = WshShell.CreateShortcut(strDesktop & "\sb.lnk")
oShellLink.TargetPath = lj4 : '目标
oShellLink.WindowStyle = 1 :'参数1默认窗口激活，参数3最大化激活，参数7最小化
oShellLink.Hotkey = "" : '快捷键
oShellLink.IconLocation = lj3 : '图标
oShellLink.Description = "sb" : '备注
oShellLink.WorkingDirectory = "" : '起始位置
oShellLink.Save : '创建保存快捷方式
MsgBox("ink make ok")