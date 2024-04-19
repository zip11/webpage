; 设置热键 Ctrl+A 读取 dmmpic 配置
^a::
result := ReadIni("dmmpic")
;MsgBox, %result%
SendString(result)
return

; 设置热键 Ctrl+S 读取 hbpic 配置
^s::
result := ReadIni("hbpic")
;MsgBox, %result%
SendString(result)
return

; 设置热键 Ctrl+D 读取 Videot_Title 配置
^d::
result := ReadIni("Videot_Title")
;MsgBox, %result%
SendString(result)
return

; 定义一个函数来发送字符串
SendString(str) {

    clipboard = %str%
    ;存到剪贴板，不然中文会有乱码
    Send ^v
    ; 将字符串发送到当前激活的窗口
    ;Send, % str
}

ReadIni(sectionName) {
    ; 获取符合匹配的 INI 文件名
    IniFilePattern := "*_Pic_Link.ini"
    Loop, Files, %IniFilePattern%
    {
        If RegExMatch(A_LoopFileName, ".*_Pic_Link\.ini")
        {
            IniFileName := A_LoopFileName
            Break
        }
    }

    ; 检查是否找到了符合条件的 INI 文件
    If (IniFileName = "")
    {
        MsgBox, 找不到符合条件的 INI 文件
        return
    }

    ; 读取 ini 文件
    IniRead, value, %IniFileName%, Section, %sectionName%
    
    ; 如果读取成功，输出配置字符串
    ;  配置 名字，配置的 值, %sectionName%: %value%
    if ErrorLevel = 0
        return %value%
    else
        MsgBox, 配置项不存在
}
