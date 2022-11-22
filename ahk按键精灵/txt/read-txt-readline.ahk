#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Loop, read, D:\app\net\百灵快传\files\apk\cili.txt
{
    Loop, parse, A_LoopReadLine, %A_Tab%
    {
        MsgBox, Field number %A_Index% is %A_LoopField%.
    }
}