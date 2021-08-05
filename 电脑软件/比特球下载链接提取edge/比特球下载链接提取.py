##edge下载列表，获取bitqiu网址
#生成aria2下载命令
import re
import win32clipboard as w
import win32con  

nwz = ""
arml = "aria2c -s 3 -x 3 -c --user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71' "

def getText():#读取剪切板  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_TEXT)  
    w.CloseClipboard()  
    return d  

def setText(aString):#写入剪切板  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardText(aString)  
    w.CloseClipboard()  


print("edge下载列表，获取bitqiu网址比特球")
regular = re.compile(r'https://\w{2}-edge-file.bitqiu.com/file/.*sign.[A-Za-z0-9]{32}')
#[\w]{32}
F = getText()
#获取剪贴板

a1=F.decode("gb2312")
#字节 转 字符串

wz1 = re.findall(regular, a1)



for colour in wz1:

    
    #nwz = nwz + arml + '\"' +colour + '\"' + '\r\n'
    nwz = nwz + colour + '\r\n'


print(nwz)
setText(nwz)
#必须字符串