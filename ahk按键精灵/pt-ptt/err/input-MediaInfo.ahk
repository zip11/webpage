#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;shift+a 

InputBox, iniInput, ini file, Please enter ini file name, , 640, 480

txtfile = %iniInput%.txt

inifile = %iniInput%.ini


; MsgBox %iniInput%


FileRead, Contents, %txtfile%

msgbox %Contents%

;~~~~~ filename

; inifile := "pz.ini"

; msgbox %inifile%           

;~~~~~ chinesetitle ~~~~~~~~~~~~




try {
    IniWrite, %Contents%, %inifile%, Section, mediainfo
    ;MsgBox, The value is %OutputVar%.
} catch e {
    msgbox e
}