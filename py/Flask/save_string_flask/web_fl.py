#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# flask 
# 网页 get，读取 配置文件的 变量
# 网页get，保存变量 到 配置文件

# 保存 配置文件~~~~~~~
import pickle
 
# Restore from a file

 
class save_read_write:
   
    '所有员工的基类'
    empCount = 0
    nr1 = ""

    def __init__(self, filepath):

        self.filepath = filepath
        # self.nr1 = nr1

        save_read_write.empCount += 1
   
    # 读取 配置文件   
    def readsave(self):

        f = open(self.filepath, 'rb')
        # rb r-read , b-binary

        data = pickle.load(f)

        f.close()

        return data

    # 写入 配置文件
    def write_save(self):

        
        # Some Python object

        f = open(self.filepath, 'wb')

        pickle.dump(self.nr1, f)

        f.close()


# 保存 读取 配置文件

pz1 = save_read_write('savefile')

# end~~~~~~~~~

# ~~~~~flask~~~~~~start~~~~~

from flask import Flask, request

app = Flask(__name__)

# 保存字符串 到 变量
@app.route('/api/get')

# http://127.0.0.1:5000/api/get?name=xyz

def testGet():
    
    name = request.args.get('name')

    print("Link:  \n",name,"\n")

    # 保存变量 到 配置文件
    pz1.nr1 = name
    pz1.write_save()

    return "get方法获取参数: \"" + name + '"' 


# 读取 之前保存 字符串
@app.route('/api/read')

# http://127.0.0.1:5000/api/read

def readGet():

    # 读取 配置文件
    vnam = pz1.readsave()
    return vnam
 
if __name__ == '__main__':
    
    app.run(debug=True)