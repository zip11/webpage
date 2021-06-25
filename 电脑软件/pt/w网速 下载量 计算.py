import os
a = input("input netspeed  Mbps :")
a =int(a)
day1 = a*60*60*24/8/1024

print("24h download",day1,"GB")
os.system("pause")