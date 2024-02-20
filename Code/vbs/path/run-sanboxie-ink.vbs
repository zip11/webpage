' get folder-name
Function GetFolderName(DriveSpec)

    Dim fso
    Set fso = CreateObject("Scripting.FileSystemObject")
    GetAName = fso.GetParentFolderName(DriveSpec)

    GetFolderName= GetAName

End Function

' get file-name
Function GetFileName(DriveSpec)

    Dim fso
    Set fso = CreateObject("Scripting.FileSystemObject")
    GetAName = fso.GetFileName(DriveSpec)

    GetFileName = GetAName
End Function

' single path
Set objArgs = WScript.Arguments
lj = objArgs(0)

' add ""
lj1 =  chr(34) & lj & chr(34)

sdlj1 = """C:\Program Files\Sandboxie-Plus\Start.exe"""
ljall = sdlj1 & " /box:DefaultBox " & lj1

data=ljall

set fs =createobject("scripting.filesystemobject")

dim inkname,exename
exename = GetFileName(lj)

inkname = GetFolderName(lj) & "\" & exename & "-qd.cmd"

' make run cmd
set f = fs.opentextfile(inkname,2, true)
f.write data
f.close

msgbox("exe-cmd run sandbox")


