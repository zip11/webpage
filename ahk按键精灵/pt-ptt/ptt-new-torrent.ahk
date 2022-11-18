#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;shift+a 

InputBox, iniInput, ini file, Please enter ini file name, , 640, 480

inifile = %iniInput%.ini

; MsgBox %iniInput%
+a::


;~~~~~ filename

; inifile := "pz.ini"

; msgbox %inifile%           



IniRead, OutputVar, %inifile%, Section, filename
;MsgBox, The value is %OutputVar%.

clipboard = %OutputVar%
;存到剪贴板，不然中文会有乱码
Send ^v
Sleep, 666

Send, {Tab}
Sleep, 666

;~~~~~ chinesetitle ~~~~~~~~~~~~

IniRead, OutputVar, %inifile%, Section, chinesetitle
;MsgBox, The value is %OutputVar%.

clipboard = %OutputVar%
;存到剪贴板，不然中文会有乱码
Send ^v
Sleep, 666

Send, {Tab}
Sleep, 666


;~~~~~~ hbpic ~~~~~~~~~~~  

IniRead, OutputVar, %inifile%, Section, hbpic
;MsgBox, The value is %OutputVar%.

clipboard = %OutputVar%
;存到剪贴板，不然中文会有乱码
Send ^v
Sleep, 666

Send, {Tab}
Sleep, 666

;~~~~~~~ dmmpic ~~~~~~~~~~

loop , 13
{
    Send, {Tab}
    Sleep, 666

}

IniRead, OutputVar, %inifile%, Section, dmmpic
;MsgBox, The value is %OutputVar%.

clipboard = %OutputVar%
;存到剪贴板，不然中文会有乱码
Send ^v
