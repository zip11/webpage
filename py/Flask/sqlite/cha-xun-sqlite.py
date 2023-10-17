# coding:utf-8

import sqlite3

# 创建或连接数据库
conn = sqlite3.connect("test.db")

# 查询数据
cursor = conn.execute("SELECT * FROM user")

# rows 行，cursor 光标

for row in cursor.fetchall():
    print(row)

conn.close()