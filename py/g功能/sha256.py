#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#calc sha256

import os
import hashlib
 
def CalcFileSha256(filname):

    ''' calculate file sha256 '''

    with open(filname, "rb") as f:

        sha256obj = hashlib.sha256()

        sha256obj.update(f.read())

        hash_value = sha256obj.hexdigest()

        return hash_value
 
 
def CalcFileSize(filename):

    ''' calculate file size '''
    """total size, in bytes"""

    return os.stat(filename).st_size
 
print("calc file sha256 ")

file = input(" input file path:")

nsha256 = CalcFileSha256(file)

print("file sha256:"+ nsha256)

print("file-size:"+str(CalcFileSize(file)))

bjsha = input("input sha256 value:")

if(bjsha == nsha256):
    print("sha256 ok")
else:
    print("sha256 error !")