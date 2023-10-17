#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sqlite3

# 创建或连接数据库
conn = sqlite3.connect("test.db")

# 创建 user 数据库
conn.execute('''
CREATE TABLE user(
	user_id int,
	user_name text,
	password text
)
''')

# 写入数据
conn.execute("INSERT INTO user (user_id,user_name,password) VALUES(1,'zmister','123456')")
conn.execute("INSERT INTO user (user_id,user_name,password) VALUES(2,'mrdoc','234323')")
conn.execute("INSERT INTO user (user_id,user_name,password) VALUES(2,'python','hahaheheh')")


conn.commit()