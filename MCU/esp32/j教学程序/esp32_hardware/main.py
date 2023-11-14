

import esp32

cl1=esp32.hall_sensor()     # read the internal hall sensor
print("magent:",cl1)

wd1=esp32.raw_temperature() # read the internal temperature of the MCU, in Fahrenheit
print("temp:",(wd1-32)/1.8,"℃")

import esp

fsz=esp.flash_size()
print("flash_size",fsz/1024/1024,"MB")
#esp32.ULP()             # access to the Ultra-Low-Power Co-processor


import machine

fq1=machine.freq()          # 获取CPU当前工作频率
print("cpu",fq1/1000/1000,"MHz")        