import os
a = input(" 输入硬盘剩余容量 GB :")
a =int(a)

b = input(" 输入下载速度 MB/S:")
b =int(b)

day1 = a*1024
day1 = day1/60/60/24

print("download time",day1,"DAY")
os.system("pause")