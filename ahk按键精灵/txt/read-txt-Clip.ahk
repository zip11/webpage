#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

CoordMode,Mouse,Client 
;读取txt ，复制视频文件名 ，到chrome 搜索 视频

Loop

{    
    FileReadLine, line, bt.txt ,%A_Index%    
    
    if ErrorLevel
        break
    
    ; read txt ,video name
    MsgBox, 4, , Copy-Video-Name-To-Clip,Line #%A_Index% is "%line%".  Continue?
    
    
    ; no exit app
    IfMsgBox, No
        return

    ; name to clip
    clipboard =  %line%
    
    ; wait chrome active
    WinWaitActive,搜索 - 98堂[原色花堂] - Powered by Discuz! - Iron
    Sleep, 4000

    ; click text area ,active
    Click 553, 242 
    
    ; all select text
    Send ^a
    Sleep, 1000
    
    ; delete all text
    Send {Backspace}
    Sleep, 1000

    ; copy text
    Send ^v
    Sleep,1000

    ; search text
    Send, {Enter}

}

MsgBox, The end of the  text file 