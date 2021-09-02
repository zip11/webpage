#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
;向下滚动减少音量
;向上滚动增加音量
;鼠标中键或滚轮切换静音

if MouseIsOver("PotPlayer64")

WheelDown::
WheelUp::
MButton::
Send, %  InStr(A_ThisHotkey,"Down") ? "{left}":InStr(A_ThisHotkey,"Up") ? "{Right}":"{Volume_Mute}"
return
;取鼠标下窗口类名对比
MouseIsOver( WinClass) {
    MouseGetPos,,,Win
	WinGetClass,WinC,ahk_id %Win% ;取窗口类名
    return InStr(WinClass,WinC)
}