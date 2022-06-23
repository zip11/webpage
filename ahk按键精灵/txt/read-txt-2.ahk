#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.



Loop
{    
    FileReadLine, line, D:\app\net\百灵快传\files\apk\cili.txt ,%A_Index%    
    if ErrorLevel
        break
    MsgBox, 4, , Line #%A_Index% is "%line%".  Continue?
    IfMsgBox, No
        return
}
MsgBox, The end of the file has been reached or there was a problem.return
