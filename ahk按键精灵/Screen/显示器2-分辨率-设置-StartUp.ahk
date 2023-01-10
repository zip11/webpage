﻿#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


; https://www.autohotkey.com/boards/viewtopic.php?f=6&t=77664
; 获取监视器2的分辨率

; MsgBox % ScreenResolution_Get("\\.\DISPLAY2")
; 获取监视器2所有屏幕分辨率的有效匹配列表

; MsgBox % ScreenResolution_List("\\.\DISPLAY2")

; 修改监视器1的分辨率
;MsgBox % ScreenResolution_Set("1280x720@60", "\\.\DISPLAY1")
; 这样写可检测监视器1是否存在，返回0为存在并启动，返回-1为存在但没启用，返回-2为监视器不存在


WinWaitActive, Paperlike Pro, , 59

if ErrorLevel
{
    MsgBox, WinWait timed out.
    return
}
else
{

  jg1 := ScreenResolution_Set("1680x1050@60", "\\.\DISPLAY2")

  if jg1 = 0
  {
    ;MsgBox "screen2 set Resolution ok"
     WinMinimize
  }
  Else
    MsgBox "screen2 set Resolution error"

}


ScreenResolution_Get(Disp:=0) {              ; v0.90 By SKAN on D36I/D36M @ tiny.cc/screenresolution
Local DM, N:=VarSetCapacity(DM,220,0) 
Return DllCall("EnumDisplaySettingsW", (Disp=0 ? "Ptr" : "WStr"),Disp, "Int",-1, "Ptr",&DM)=0 ? ""
     : Format("{:}x{:}@{:}", NumGet(DM,172,"UInt"),NumGet(DM,176,"UInt"),NumGet(DM,184,"UInt")) 
}

ScreenResolution_List(Disp:=0) {             ; v0.90 By SKAN on D36I/D36M @ tiny.cc/screenresolution
Local DM, N:=VarSetCapacity(DM,220,0), L:="", DL:=","
  While DllCall("EnumDisplaySettingsW", (Disp=0 ? "Ptr" : "WStr"),Disp, "Int",A_Index-1, "Ptr",&DM)
  If ( NumGet(DM,168,"UInt")=32 && NumGet(DM,184,"UInt")>59)
    L.=Format("{:}x{:}@{:}" . DL, NumGet(DM,172,"UInt"),NumGet(DM,176,"UInt"),NumGet(DM,184,"UInt")) 
Return RTrim(L,DL) 
}


ScreenResolution_Set(WxHaF, Disp:=0) {       ; v0.90 By SKAN on D36I/D36M @ tiny.cc/screenresolution
Local DM, N:=VarSetCapacity(DM,220,0), F:=StrSplit(WxHaF,["x","@"],A_Space)
Return DllCall("ChangeDisplaySettingsExW",(Disp=0 ? "Ptr" : "WStr"),Disp, "Ptr",NumPut(F[3]
     , NumPut(F[2], NumPut(F[1], NumPut(32, NumPut(0x5C0000, NumPut(220,DM,68,"UShort")+2,"UInt")+92
     , "UInt"),"UInt"),"UInt")+4,"UInt")-188, "Ptr",0, "Int",0, "Int",0)  
}



