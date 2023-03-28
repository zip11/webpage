## shutil模块-拷贝操作 ##

    import shutil

	# 复制文件
    shutil.copyfile('C:\\1.txt', 'D:\\1.txt')
	#oldfile和newfile都只能是文件

    shutil.copy("oldfile","newfile") 
    #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录


##     复制文件夹： ##

    shutil.copytree("olddir","newdir") 
	#olddir和newdir都只能是目录，且newdir必须不存在



## 移动文件（目录） ##

    shutil.move("oldpos","newpos") 
