#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.

SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

CoordMode,Mouse,Client 
CoordMode,Pixel,Client

sleep 3000

loop
{




    PixelGetColor, color,755, 239,Alt
    MsgBox %color%
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