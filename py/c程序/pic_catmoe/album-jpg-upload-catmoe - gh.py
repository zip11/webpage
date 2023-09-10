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


# api hash
uhash = ''
# album link id
albid = ''
# file name
filestr = ''

proxies = {

		'https': 'socks5://192.168.2.2:1111'
}

def add_album(hash,albid1,filestr1):

	# 上传参数

# Adding files to an album

# reqtype="addtoalbum" 
# userhash="####" 
# short="pd412w" 
# files="8ce67f.jpg f51d7d.jpg 65ea43.jpg"
	
	files = {

		'reqtype': ('addtoalbum'),
		# api
		'userhash': (hash),
		'short': (albid1),
		'files' : (filestr1)

	}

	# 代理



	# 上传 post
	response = requests.post('https://catbox.moe/user/api.php', data=files, proxies=proxies)

	# 返回jpg网址
	# jpg link 
	jpglink = ''
	jpglink = response.text

	print("add-album:" + jpglink)

	return jpglink
	


def create_album(hash,title1,desc1,filestr1):

# Creating an album

# reqtype="createalbum" 
# userhash="####" 
# title="Title Here" 
# desc="Description Here" 
# files="8ce67f.jpg f51d7d.jpg 65ea43.jpg"

	# 上传参数
	files = {

		'reqtype': ('createalbum'),
		# api
		'userhash': (hash),
		'title': (title1),
		'desc': (desc1),
		'files' : (filestr1)

	}

	# 代理
	proxies = {
		# 'http': 'socks5://192.168.2.7:20170',
		'https': 'socks5://192.168.2.7:20170'
	}


	# 上传 post
	response = requests.post('https://catbox.moe/user/api.php', data=files, proxies=proxies)

	# 返回jpg网址
	# jpg link 
	jpglink = ''
	jpglink = response.text

	print("create-album:" + jpglink)

	return jpglink
	


# ~~~~ main ~~~~~~~~~~~

print('https://catbox.moe ,upload jpg ,save pic link to txt')

# create_album()
# hash,
# albid,
# filestr 

# 添加 照片 到 相册
add_album(uhash,albid,filestr)

# 创建 相册
# create_album(uhash,title,desc,filestr)

