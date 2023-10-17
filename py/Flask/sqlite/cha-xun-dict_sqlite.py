# coding:utf-8

import sqlite3

def dict_factory(cursor, row):

    d = {}

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d

# 创建或连接数据库
conn = sqlite3.connect("test.db")

conn.row_factory = dict_factory

# 查询数据
cursor = conn.execute("SELECT * FROM user")

for row in cursor.fetchall():
    print(row)

conn.close()