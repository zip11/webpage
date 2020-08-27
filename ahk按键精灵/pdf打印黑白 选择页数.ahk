#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;pdf 打印默认黑白，选择页数,foxit pdf阅读软件
#a::

send ^p
Sleep 1000
;打开打印选项

send {Tab 19}
Sleep 1000

send {Space}
Sleep 1000
;选择黑白打印

send {Tab 3}
Sleep 1000

send  {Down 2}
Sleep 1000

send {Tab 1}
;选择页数


Exit

#s::
ExitApp