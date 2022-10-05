#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# https://imgbb.com/

# 上传jpg 图床，获取jpg网址

import os

import requests

import json

# 上传 图片
def uploadjpg():

	jpglj = input("jpg  drop path:")

	# jpglj = 'ts1.PNG'

	# 获取 文件名
	jpgwjm = os.path.basename(jpglj)

	# 读取 jpg 二进制
	f = open(jpglj,'rb')
	jpgnr = f.read()

	# API
	params = {
		'expiration': '600',
		'key': 'b11111',
	}

	files = {
		# 文件名 ，jpg 二进制 内容
		'image': (jpgwjm, jpgnr),
	}
	# post 上传
	response = requests.post('https://api.imgbb.com/1/upload', params=params, files=files)

	# json 转换 dict
	upjg = json.loads(response.text)

	# print(upjg)

	# jpg link 
	jpglink = upjg['data']['url']
	
	print(jpglink)
	return jpglink


print('https://imgbb.com/ ,upload jpg ,save txt')

# jpg Link list
jpgl = []

while True:

	# upload jpg
	jpgwz =  uploadjpg()

	#  BBcode
	jpgwz = '[img]' + jpgwz + '[/img]'

	print(jpgwz)
	
	# add jpg list
	jpgl.append(jpgwz)

	kcode = input("upload jpg (Enter) Or Exit (q)")
	
	# Exit  
	if kcode == 'q':
		
		# txt Save jpg-wz
		f=open("ptt.txt","w")
		f.writelines(jpgl)
		f.close()
		print('Exit , jpg bbcode save Txt')

		break




