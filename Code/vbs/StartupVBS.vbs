; ��ӿ�������������ʱ��������Ϊ��λ��vbs��if�жϣ���ʹĿ�겻����Ҳ���ᱨ��
PowerBoot(VBSFileName:="StartupVBS", Sleep:=0, StartupPath:="") {

    FileDelete, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
    StartupPath := StartupPath="" ? A_ScriptFullPath : StartupPath
    FileAppend, Set shell=CreateObject("Wscript.Shell")`nSet fs=CreateObject("Scripting.FileSystemObject")`nif fs.FileExists("%StartupPath%") then`nWscript.Sleep 1000*%Sleep%`nshell.Run"""%StartupPath%"""`nend if, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
    
    Return ErrorLevel
}


; ɾ��������
DeletePowerBoot(VBSFileName:="StartupVBS") {

	FileDelete, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
}


; ��鿪���������ű�·���Ƿ���ȷƥ�䡾��ȷ����0�����󷵻�1��
ExaminePowerBoot(VBSFileName:="StartupVBS", StartupPath:="") {

    FileRead, VBSContent, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
    StartupPath := StartupPath="" ? A_ScriptFullPath : StartupPath
	
    Return InStr(VBSContent, StartupPath)=0 ? 1 : 0
}