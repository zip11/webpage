dim lj4
lj4 = "c:\123.exe"
Set WshShell = WScript.CreateObject("WScript.Shell")
strDesktop = WshShell.SpecialFolders("Desktop") :'特殊文件夹“桌面”
set oShellLink = WshShell.CreateShortcut(strDesktop & "\sb.lnk")
oShellLink.TargetPath = lj4 : '目标
oShellLink.WindowStyle = 1 :'参数1默认窗口激活，参数3最大化激活，参数7最小化
oShellLink.Hotkey = "" : '快捷键
oShellLink.IconLocation = lj4 : '图标
oShellLink.Description = "sb" : '备注
oShellLink.WorkingDirectory = "" : '起始位置
oShellLink.Save : '创建保存快捷方式
MsgBox("ink make ok")