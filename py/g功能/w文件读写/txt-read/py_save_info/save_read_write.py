#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pickle
 
# Restore from a file

 
class save_read_write:
   
    '所有员工的基类'
    empCount = 0

    def __init__(self, filepath, nr1):

        self.filepath = filepath
        self.nr1 = nr1

        save_read_write.empCount += 1
   
    # 读取 配置文件   
    def readsave(self):

        f = open(self.filepath, 'rb')
        # rb r-read , b-binary

        data = pickle.load(f)

        f.close()

        return data

    # 写入 配置文件
    def write_save(self,nr1):

        
        # Some Python object

        f = open(self.filepath, 'wb')

        pickle.dump(self.nr1, f)

        f.close()



data = {1,3,5} 

pz1 = save_read_write('savefile',data)

pz1.write_save()
print("save list to file end!!!!")

data1 = pz1.readsave()
print("read_file_text:",data1)
