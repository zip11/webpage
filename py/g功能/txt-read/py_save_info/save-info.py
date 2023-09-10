#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pickle
 


def write_save(file_path,nr2):

    
    # Some Python object

    f = open(file_path, 'wb')

    pickle.dump(nr2, f)

    f.close()

    print("save list to file end!!!!")

    
data = {1,3,5} 

write_save('savefile',data)