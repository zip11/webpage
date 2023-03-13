Python使用shutil.move


shutil.move('原文件完整路径(带文件名)','目标文件夹')


## 1. 文件已存在目标文件夹会报错 ##

解决方案:通过exists方法判断

    import os
    import datetime 
	#重命名加时间戳用

    def path_file_isexist(uFilepath,uFolder): 

    	if os.path.exists(os.path.join(uFolder,uFilepath.split('\\')[-1])):
			
			#目标文件夹+要移动的文件名

    		newFilepath='{0}_{1}.{2}'.format(uFilepath.split('.')[0],datetime.datetime.now().strftime('%Y%m%d%H%M%S'),uFilepath.split('.')[-1])#存在,则切割成:原文件路径(不带格式)_时间戳.原文件格式
    		os.rename(uFilepath,newFilepath) # 重命名
    		return newFilepath # 返回新文件路径
    	else:
    		return uFilepath # 不重复,返回原路径


## 2. 目标文件夹不存在会报错 ##

		

    import os

    def path_folder_isexist(uDir):
    
    if os.path.exists(uDir):
    	return uDir # 有这个文件夹,直接返回原路径
    else:
    	os.mkdir(uDir) # 没有这个文件夹,就创建一个
    	return uDir # 返回新路径
    		
		
## 3. 程序正在使用会报错 ##

这是个无解的Bug,如果杀进程那每次都要调整预期的程序,比较麻烦.所以我直接try…except…捕捉错误了.伪代码如下

    import shutil
    def action_move(uF):
    	try:
    		shutil.move(uFile,uFolder) #尝试移动
    	except Exception as e:
    		print(e) #移动不成功,打印报错信息
    	pass


————————————————
版权声明：本文为CSDN博主「但老师」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/sinat_41870148/article/details/105754119
