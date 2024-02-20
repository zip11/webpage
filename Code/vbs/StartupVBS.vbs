; 添加开机自启动，延时功能以秒为单位【vbs带if判断，即使目标不存在也不会报错】
PowerBoot(VBSFileName:="StartupVBS", Sleep:=0, StartupPath:="") {

    FileDelete, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
    StartupPath := StartupPath="" ? A_ScriptFullPath : StartupPath
    FileAppend, Set shell=CreateObject("Wscript.Shell")`nSet fs=CreateObject("Scripting.FileSystemObject")`nif fs.FileExists("%StartupPath%") then`nWscript.Sleep 1000*%Sleep%`nshell.Run"""%StartupPath%"""`nend if, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
    
    Return ErrorLevel
}


; 删除自启动
DeletePowerBoot(VBSFileName:="StartupVBS") {

	FileDelete, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
}


; 检查开机自启动脚本路径是否正确匹配【正确返回0，错误返回1】
ExaminePowerBoot(VBSFileName:="StartupVBS", StartupPath:="") {

    FileRead, VBSContent, %A_StartMenu%\Programs\Startup\%VBSFileName%.vbs
    StartupPath := StartupPath="" ? A_ScriptFullPath : StartupPath
	
    Return InStr(VBSContent, StartupPath)=0 ? 1 : 0
}