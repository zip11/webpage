; This script was created using Pulover's Macro Creator
; www.macrocreator.com

#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window
SendMode Input
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 1
SetWinDelay 0
SetKeyDelay -1
SetMouseDelay -1
SetBatchLines -1


F4::
quark:

InputBox, UserInput,  Number, Please enter file download number 8., , 640, 480
if ErrorLevel
    MsgBox, CANCEL was pressed.
else
    MsgBox, You entered "%UserInput%"

If(UserInput == ""){

   UserInput := 8
   MsgBox, You entered "%UserInput%"

}

WinActivate, ahk_class Chrome_WidgetWin_1  ; 激活 edge 窗口
Sleep, 333

WinWaitActive, ahk_class Chrome_WidgetWin_1  ; 等待 游览器 激活 窗口
Sleep, 333

Click, 358, 343 Left, 1  ;  点击 全选 方框
Sleep, 10
Sleep, 300
Click, Left, 1  ; end 全选
Sleep, 10



Loop, %UserInput%  ; 循环 选择 方框
{
Send, {Tab}
Sleep, 1000
Send, {Space}
}
Return

