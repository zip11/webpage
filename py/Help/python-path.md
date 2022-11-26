### os.listdir 获取文件夹下所有文件



os.listdir：参数为文件夹路径，可以返回文件夹下的所有子文件夹、文件名称。

import os

path = 'D:\Workspace'
for file_name in os.listdir(path):
    print(file_name)


### os.chdir() 

将当前工作目录切换到指定的路径。


### os.getcwd()

获取当前 工作目录

### os.rename() 

方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

### os.walk

参数为文件夹路径，返回3个内容：绝对路径、子文件夹、文件名。 此方法可以遍历文件夹下的所有文件、子文件及内的所有文件：

import os

path = 'D:\Workspace'
for root, dirs, files in os.walk(path):
    print(root)
    print(dirs)
    print(files)


### glob.glob

glob：参数为路径以及文件过滤条件，若不设置过滤需填写为*，此函数会返回包括路径的文件夹和文件名
示例：

import glob

path = 'D:\Workspace\folder\*'
for file_abs in glob.glob(path):
    print(file_abs)
