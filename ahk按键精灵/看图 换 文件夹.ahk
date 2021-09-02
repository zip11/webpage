#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;功能：输入法状态提示
;环境：win10+搜狗输入法，输入法状态切换用默认的shift键。
;作者：sunwind
;时间：2018年9月1日
;更新链接：https://blog.csdn.net/liuyukuan/article/details/82291632
 

XButton2::
SendRaw {[}