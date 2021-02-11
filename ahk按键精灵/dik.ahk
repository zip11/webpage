#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; 示例 #1: 这是个可运行脚本, 它添加一个新菜单项到托盘图标菜单的底部.
 
#Persistent ; 让脚本持续运行, 直到用户退出.
Menu, tray, add ; 创建分隔线.
Menu, tray, add, Item1, MenuHandler ; 创建新菜单项.

bbh = ahk_class  SDL_app

return

XButton2:: 
; 鼠标上键

;窗口缩小
WinMove,%bbh% ,,,,800,600
return       


XButton1:: 
; 鼠标下键

;窗口最小化
WinMinimize,%bbh%




MButton::
;鼠标中键

;调整文本大小
Loop 20
{
    SendRaw {Space down}  ; 自动重复由连续的按下事件组成 (没有弹起事件).
    Sleep   999  ; 在两次键击之间的毫秒数 (或使用 SetKeyDelay 设置).
}
SendRaw {Space up} 


#A::
reload

 
MenuHandler:
MsgBox You selected %A_ThisMenuItem% from menu %A_ThisMenu%.
return
