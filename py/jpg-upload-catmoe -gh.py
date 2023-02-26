#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# https://catbox.moe

# 上传jpg 图床，获取jpg网址 ,save jpg link txt

import os

import requests

# api user hash
userhash1 = ""

# 上传 图片
def uploadjpg():

	jpglj = input("jpg file  drop here ,Enter:")

	# 正常化 地址
	jpglj =  os.path.normpath(jpglj)

	#print('jpg path',jpglj)
	# jpglj = 'ts1.PNG'

	# 获取 文件名
	jpgwjm = os.path.basename(jpglj)

	# 读取 jpg 二进制
	f = open(jpglj,'rb')
	jpgnr = f.read()

	# 上传参数
	files = {
		'reqtype': (None, 'fileupload'),
		# api ,'123456'
		'userhash': (None,userhash1 ),
		# jpg file name , jpg binary
		'fileToUpload':(jpgwjm,jpgnr),
	}

	response = requests.post('https://catbox.moe/user/api.php', files=files)



	# 返回jpg网址
	# jpg link 
	jpglink = ''
	jpglink = response.text

	print(jpglink)

	return jpglink


# ~~~~ main ~~~~~~~~~~~

print('https://catbox.moe ,upload jpg ,save txt')

# jpg Link list
jpgl = []

# 循环上传 jpg
while True:

	# upload jpg
	jpgwz =  uploadjpg()

	# #  BBcode
	jpgwz = '[img]' + jpgwz + '[/img]\n\n'

	#print(jpgwz)
	
	# add jpg list
	jpgl.append(jpgwz)

	kcode = input("upload jpg (Enter) Or Exit (q)\n")
	
	# Exit  
	if kcode == 'q':
		
		# txt Save jpg-wz
		f=open("ptt-cat.txt","w")
		f.writelines(jpgl)
		f.close()

		print('Exit , jpg bbcode save Txt')

		break




