#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


#If MouseIsOver("Shell_TrayWnd|WorkerW|Progman") ;在鼠标放在带指定关键字窗口类名下可用滚轮调节系统音量
WheelDown::
WheelUp::
MButton::
Send, %  InStr(A_ThisHotkey,"Down") ? "{Volume_Down}":InStr(A_ThisHotkey,"Up") ? "{Volume_Up}":"{Volume_Mute}"
SoundGet, OutputVar
vol:=Format("{:d}", OutputVar)
ToolTip,% "音量 " repeat("█",vol/2) vol "%" repeat(" ",100-vol) ,A_ScreenWidth/2-250,A_ScreenHeight-55
SetTimer, RemoveToolTip, 2000
return
#If ;-------------------[调节音量]--区域结束-------------------
RemoveToolTip:
ToolTip
return
;取鼠标下窗口类名对比
MouseIsOver( WinClass) {
    MouseGetPos,,,Win
  WinGetClass,WinC,ahk_id %Win% ;取窗口类名
    return InStr(WinClass,WinC)
}
;生成指定数量的指定字符
repeat(_str,_int) {
Loop,% _int
  _str_.=_str
return _str_
}



