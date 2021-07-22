#文件放入启动器，同一个文件夹

import win32api     # 导入win32api模块  
import win32con    # 导入win32con模块  
import configparser

wjm = "AWLoader.ini"
x1 = input("输入程序文件夹")
x2 = x1 + "Distrib\\"


cfp = configparser.ConfigParser()
cfp.read(wjm)

cfp.set("Main", "GamesInstallPath", x1)
cfp.set("Main", "DownloadPath", x2)


with open(wjm, "w+") as f:
    cfp.write(f)


# key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,  
# 'Software\AWChina\Armored Warfare Kongzhong',0,win32con.KEY_WRITE)  
# print("key:",key)

# jg = win32api.RegSetValueEx(key,'InstallLocation',0,win32con.REG_SZ,x1)  

# print("jg:",jg)