#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 读取csv文件
import csv

with open('test.csv','r') as myFile:

    lines=csv.reader(myFile)

    for line in lines:
        print (line)