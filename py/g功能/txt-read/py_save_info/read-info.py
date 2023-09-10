#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pickle
 
# Restore from a file



def readsave(save_filepath):

    f = open(save_filepath, 'rb')
    # rb r-read , b-binary

    data = pickle.load(f)
    
    print(data)

    f.close()
    
    return data

# Restore from a string
# data = pickle.loads(s)

readsave("savefile")