;等待 窗口 激活，Paperlike Pro

; wait 19s
WinWaitActive, Paperlike Pro, , 19

if ErrorLevel
{
    MsgBox, WinWait timed out.
    return
}
else
    WinMinimize  ; 最小化 WinWaitActive 找到的窗口.