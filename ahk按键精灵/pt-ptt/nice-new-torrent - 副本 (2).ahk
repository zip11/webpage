#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;shift+a 
;nice pt,new torrent

InputBox, iniInput, ini file, Please enter ini file name, , 640, 480

inifile = %iniInput%.ini
txtfile = %iniInput%.mp4.txt

; MsgBox %iniInput%

;shift+a 
+a::


;~~~~~ filename

; inifile := "pz.ini"

; msgbox %inifile%           

;----Title----

IniRead, OutputVar, %inifile%, Section, filename
;MsgBox, The value is %OutputVar%.

clipboard = %OutputVar%
;存到剪贴板，不然中文会有乱码
Send ^v
Sleep, 666

Send, {Tab}
Sleep, 666

Send, {Tab}
Sleep, 666

;~~~~~ Sub-chinese-title ~~~~~~~~~~~~

IniRead, OutputVar, %inifile%, Section, chinesetitle
;MsgBox, The value is %OutputVar%.

clipboard = %OutputVar%
;存到剪贴板，不然中文会有乱码
Send ^v
Sleep, 666

Send, {Tab}
Sleep, 666


;~~~~~~ hb-pic ~~~~~~~~~~~  

IniRead, OutputVar, %inifile%, Section, hbpic
;MsgBox, The value is %OutputVar%.

fmpic := OutputVar
fmpic = [img]%fmpic%[/img]
;存到剪贴板，不然中文会有乱码
; Send ^v
; Sleep, 666

Send, {Tab}
Sleep, 333

;~~~~~~~ dmm-pic-duo ~~~~~~~~~~

loop , 14
{
    Send, {Tab}
    Sleep, 666

}

IniRead, OutputVar, %inifile%, Section, dmmpic
;MsgBox, The value is %OutputVar%.

fmpic = %fmpic%%OutputVar%

clipboard = %fmpic%
;存到剪贴板，不然中文会有乱码
Send ^v

; ---media info ----

loop , 35
{
    Send, {Tab}
    Sleep, 333

}


FileRead, Contents, %txtfile%

clipboard = %Contents%
;存到剪贴板，不然中文会有乱码
Send ^v
