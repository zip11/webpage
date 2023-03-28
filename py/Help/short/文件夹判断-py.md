## 文件夹 判断 ##

    import os

    if os.path.isdir(path):
	    print "it's a directory"
    elif os.path.isfile(path):
	    print "it's a normal file"
    else:
	    print "it's a special file(socket,FIFO,device file)"



## 判断文件或文件夹是否存 ##

import os
os.path.exists(test_file.txt)
#True

os.path.exists(no_exist_file.txt)
#False

