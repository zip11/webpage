#!/usr/bin/python3
# -*- coding: UTF-8 -*-

 # image file 转 base64

if __name__ == '__main__':

   
    import base64

    lj1 = input("input pic file:")
    
    with open(lj1,"rb") as f:
        
        #转为二进制格式
    
        base64_data = base64.b64encode(f.read())
        #使用base64进行加密
        
        # byte to str
        str64 = base64_data.decode()
        print(str64)

        # clipboard
        import pyperclip
        pyperclip.copy(str64)
        pyperclip.paste()
    
        # file=open('1.txt','wt')#写成文本格式
        # file.write(base64_data)
        # file.close()
