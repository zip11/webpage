#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import csv

with open('test.csv','w+') as myFile:

    myWriter=csv.writer(myFile)

    # writerrow一行一行写入
    myWriter.writerow([7,8,9])
    myWriter.writerow([8,'h','f'])

    # writerow多行写入
    myList=[[1,2,3],[4,5,6]]
    myWriter.writerows(myList)