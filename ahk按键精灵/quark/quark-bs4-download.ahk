#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;bs4模拟器 

WinActivate, BlueStacks App Player  ; 激活 窗口
Sleep, 333
WinWaitActive, BlueStacks App Player  ; 等待 激活 窗口
Sleep, 333
WinMove, A,, 538, 0, 580, 998  ; 窗口位置，窗口大小
Sleep, 333

Click, 472, 839 Left, 1  ; 点击 +
Sleep, 1000

Click, 450, 491 Left, 1  ; 点击 bt 磁力
Sleep, 1000

Click, 321, 121 Left, 1  ; 点击 选择输入 磁力链接
Sleep, 2000

Loop
{    
    FileReadLine, line, D:\app\net\百灵快传\files\apk\cili.txt ,%A_Index%    
    
    if ErrorLevel = 1
    {
        Break
    }


    ;MsgBox, 4, , Line #%A_Index% is "%line%".  Continue?
    Click, 248, 322 Left, 1  ; 点击 链接框
    Sleep, 1000
    ;MsgBox %line%
    
    SendInput,  %line%
    Sleep, 1000
    Click, 279, 960 Left, 1  ; 点击 下载 按钮
    Sleep, 1000

    Loop, 2
    {
        Click, 497, 114 Left, 1  ; 取消 全选文件
        Sleep, 500
    }
    
    Click, 245, 255 Left, 1  ; 点击 选择第一个 文件
    Sleep, 1000
    
    Click, 443, 947 Left, 1  ; 点击 保存网盘
    Sleep, 2000

    Click, 35, 114 Left, 1  ; 返回 键
    Sleep, 1500

    Click, 35, 114 Left, 1  ; 返回 键
    Sleep, 3500

    
}


Return







