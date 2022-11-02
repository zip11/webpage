#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;移动软件窗口到第二个 屏幕

; 移动窗口 类名
bbh = ahk_class Chrome_WidgetWin_1


Sleep, 2000

;  获取窗口位置
WinGetPos, X, Y, , , %bbh%  
; %bbh% 表示获取活动窗口的位置.

;MsgBox, The active window is at %X%`,%Y%


if (X = 2090)
; X 第二个屏幕左上角 位置
{

    ;移动 窗口 到 第一个 屏幕
    WinActivate, %bbh%
    Sleep, 1000

    WinMove, %bbh%, , 10, 0  ;
    Sleep, 1000

    Send, {LWin}{Up}
    ;WinMaximize, %bbh%
    Sleep, 1000

    return
}
Else
{

    ;移动 窗口 到 第二个 屏幕
    WinMove, %bbh%, , 2090, 0  ;

    WinActivate, %bbh%
    Sleep, 1000

    WinMaximize, %bbh%

    return
}
