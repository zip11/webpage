#!/usr/bin/python3
# -*- coding: UTF-8 -*-

 # image file 转 base64,js script use

if __name__ == '__main__':

   
    import base64

    lj1 = input("input base64 str,to pic file:")

    mz1 = input("input ico file name:")

    # del text
    lj1=lj1.replace("data:image/x-icon;base64,","")

    imgdata = base64.b64decode(lj1)
    
    #  pic file Save

    file = open('ico-'+mz1+'.png','wb')

    file.write(imgdata)
    file.close()

    print("png file save ok")

    

