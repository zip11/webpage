Function GetFolderName(DriveSpec)

    Dim fso
    Set fso = CreateObject("Scripting.FileSystemObject")
    GetAName = fso.GetParentFolderName(DriveSpec)

    GetFolderName= GetAName

End Function

'drop file
Set objArgs = WScript.Arguments
fileurl = objArgs(0)

lj = GetFolderName(fileurl)

msgbox(lj) 