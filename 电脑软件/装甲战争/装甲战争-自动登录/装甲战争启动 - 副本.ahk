#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

bbh = ahk_class  CryENGINE
CoordMode,Mouse,Client 
CoordMode,Pixel,Client

Run,"D:\app\net\AWLoader\AwLoader.exe"
WinWaitActive,启动器
sleep 4000

loop 
{
    ;检查登录按钮颜色
    PixelGetColor, color, 1194, 620
    ;MsgBox %color%
    if(color=0x1787DF)
    {
        ;MsgBox "ok run button"
        Click  1200,626
        break
    }
    else
    {
        ;超时3s，关闭脚本
        sleep 3000
        if a_index > 3
            MsgBox "error run button"
            return
    }
}

WinWaitActive,启动器 - 登录
sleep 4000

loop
{

    PixelGetColor, color,755, 239,Alt
    ;MsgBox %color%
    if(color!=0xCECCCB)

    {
        sleep 1000
        if(a_index>6)
        {
            MsgBox "password input error"
            break
        }
    }
break
}

Click 100,110
sleep 300
;获取焦点

send {Tab}
sleep 300

send {Tab}
sleep 300

send {Tab}
sleep 300


send pd
send {Enter}

WinWaitActive,%bbh%
WinMove, %bbh%, , 201,96 ;


ExitApp
