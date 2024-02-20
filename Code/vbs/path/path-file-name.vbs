Function GetFileName(DriveSpec)

    Dim fso
    Set fso = CreateObject("Scripting.FileSystemObject")
    GetAName = fso.GetFileName(DriveSpec)

    GetFileName = GetAName
End Function

'drop file
Set objArgs = WScript.Arguments
fileurl = objArgs(0)

lj = GetFileName(fileurl)

msgbox(lj) 