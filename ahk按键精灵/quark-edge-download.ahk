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


F3::
Macro1:
InputBox, UserInput,  Number, Please enter file download number 8., , 640, 480
if ErrorLevel
    MsgBox, CANCEL was pressed.
else
    MsgBox, You entered "%UserInput%"
  ; 输入 下载文件 数量
yzb := 397  ; y坐标 开始点
Loop, %UserInput%
{
    Click, 1083, %yzb% Left, 1  ; 点击 下载 文件
    Sleep, 4000
    yzb := yzb + 68  ; y 坐标 向下走 1行 
}
Return

