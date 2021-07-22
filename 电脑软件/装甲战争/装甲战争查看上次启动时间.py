import win32api     # 导入win32api模块  
import win32con    # 导入win32con模块
import time
import os
  
# 使用RegOpenKey打开注册表项  
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  
'Software\AWChina\Armored Warfare Kongzhong',0,win32con.KEY_READ)  
print(key)     # key为打开的项的句柄 

yid=win32api.RegQueryValueEx(key,'GcGameId') 

idsz=yid[0]

print("游戏id",idsz)


key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  
'Software\AWChina\Running',0,win32con.KEY_READ)


idsz=idsz+'Start'
yid=win32api.RegQueryValueEx(key,idsz) 


sjc=yid[0]

print("游戏启动时间戳",sjc)


timeStamp = int(sjc)
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)

print("游戏上次启动时间",otherStyleTime)


win32api.RegCloseKey(key)
os.system("pause")