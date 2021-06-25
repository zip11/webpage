import os
a = input(" 输入硬盘剩余容量 GB :")
a =int(a)

b = input(" 输入下载时间 ？天:")
b =int(b)

day1 = a/b/24/60/60
day1 = day1*1024*1024

print("dwonload KB/s",day1,"KB/s")
os.system("pause")