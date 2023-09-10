#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# https://catbox.moe

# 上传jpg 图床，获取jpg网址 ,save jpg link txt

# path
import os

# post
import requests

# exit
import sys

import pickle

# api hash
uhash = ''

# 代理
proxies = {
	''
}



# 上传 单个 图片
def uploadjpg(hash,jpglj):

	

	print("jpglj-ys:" + jpglj)

	# 正常化 地址
	jpglj =  os.path.normpath(jpglj)



	# 路径 空格 添加转义字符 \
	# jpglj = jpglj.replace(" ", r'\ ')

	#print('jpg path',jpglj)
	# jpglj = 'ts1.PNG'

	# 获取 文件名
	jpgwjm = os.path.basename(jpglj)

	
	jpg_folder = os.path.dirname(jpglj)
	os.chdir(jpg_folder)

	# 读取 jpg 二进制
	f = open(jpgwjm,'rb')
	jpgnr = f.read()
	# ~~~~~~~~pic read  end ~~~~~~~~~


	# 上传参数
	files = {
		'reqtype': (None,'fileupload'),
		# api
		'userhash': (hash),
		# jpg file name , jpg binary
		'fileToUpload':(jpgwjm,jpgnr)
	}

	# print(hash)


	# 上传 post
	response = requests.post('https://catbox.moe/user/api.php', files=files, proxies=proxies)

	# 返回jpg网址
	# jpg link 
	jpglink = ''
	jpglink = response.text

	print("jpglink:" + jpglink)

	return jpglink

# 上传 文件夹下-所有图片
def dirpic(dirname) :

	# 获取 文件夹下 所有 图片路径
	dirnam = os.listdir(dirname)

	# 遍历 路径 列表
	for piclj in dirnam :

		# 图片 拼接 全路径
		piclj = os.path.join(dirname,piclj)
		
		# 上传 单个 图片
		jpgwz1 = uploadjpg(uhash,piclj)
		
		# 链接 转 bbcode
		bbocde(jpgwz1)
	
	# 图片网址 保存 txt 
	pic_link_save()
	
	# 保存 图片文件名
	pic_filename_save()

# 单个图片网址-转换bbcode 格式
def bbocde(jpgwz) :
		# #  BBcode
		jpgwz = '[img]' + jpgwz + '[/img]\n\n'

		#print(jpgwz)
		
		# add jpg list
		jpgl.append(jpgwz)

# 保存

# 获取图片 链接 文件名
def picfile_name() :

	wz1 = "https://files.catbox.moe/"

	pic_file = []

	# 遍历 list
	for jpgs in jpgl:

		# 删除网址 ，得到 图片 文件名
		jpgs = jpgs.replace(wz1,'')
		pic_file.append(jpgs)
	
	return pic_file


# 保存 网站图片 文件名
def pic_filename_save() :

	 
	nr_picname = picfile_name()
	
	# 保存txt， 图片的 图床文件名
	txt_save("catmoe-filename.txt",nr_picname)

	# 序列化 文件名
	f = open('save_picfile', 'wb')
	pickle.dump(nr_picname, f)

# 图片链接-保存txt
def pic_link_save():

	txt_save("ptt-cat.txt",jpgl)

	print('jpg bbcode save Txt')


# txt 文件保存
def txt_save(txtname,nr):

		# txt Save jpg-wz
	f = open(txtname,"a")

	# w 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	# a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
	# a 也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
	
	f.writelines(nr)
	f.close()

# ~~~~ main ~~~~~~~~~~~

print('https://catbox.moe ,upload jpg ,save pic link to txt')

# jpg Link list
jpgl = []

# 循环上传 jpg
while True:

	jpglj1 = input("jpg file  drop here ,Enter:")

	# Exit  
	if jpglj1 == 'q':

		# 保存 网站 图片 链接 到txt
		pic_link_save() 


		# 退出 程序
		sys.exit(0)	


	# 判断 路径 是否 为 文件夹
	if os.path.isdir(jpglj1) :

		# 文件夹 图片上传
		print("dir-pic-upload start:")
		dirpic(jpglj1)

	else :

		# upload jpg -单个文件上传
		jpgwz2 =  uploadjpg(uhash,jpglj1)
		bbocde(jpgwz2)


	




