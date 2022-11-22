'-------------------------------------------------   
'函数名称:ReadFile   
'作用:利用AdoDb.Stream对象来读取各种格式的文本文件   
'----------------------------------------------------   
   
Function ReadFile(FileUrl)   
    Dim Str   
    Set stm = CreateObject("Adodb.Stream")   
    stm.Type = 2   
    stm.mode = 3   
    stm.charset = "utf-8"   
    stm.Open   
    stm.loadfromfile FileUrl   
    Str = stm.readtext   
    stm.Close   
    Set stm = Nothing   
    ReadFile = Str   
End Function   
   
'-------------------------------------------------   
'函数名称:WriteToFile   
'作用:利用AdoDb.Stream对象来写入各种格式的文本文件   
'参数:FileUrl-文件相对路径;Str-文件内容;CharSet-编码格式(utf- 8,gb2312.....)   
'----------------------------------------------------   
   
Function WriteToFile (FileUrl, Str)   
    Set stm = CreateObject("Adodb.Stream")   
    stm.Type = 2   
    stm.mode = 3   
    stm.charset = "gb2312"   
    stm.Open   
    stm.WriteText Str   
    stm.SaveToFile FileUrl, 2   
    stm.flush   
    stm.Close   
    Set stm = Nothing   
End Function   
 
dim fileurl 
' file path

Set objArgs = WScript.Arguments
fileurl = objArgs(0)
'msgbox(fileurl)
'drop file path

'fileurl="D:\go\src\uf.txt" 

Call writetofile(fileurl,readfile(fileurl)) 
'utf8 to gb2312
msgbox("utf8 to gb2312 ok")