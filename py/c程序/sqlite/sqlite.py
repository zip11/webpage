import os
import sqlite3

# 显示sqlite，全部表的数据
def dispaly_sqlite_all_tables(db_path):

    # 数据库文件路径
    database_path = db_path

    # 连接到SQLite数据库
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 获取所有表名
    # sqlite_master系统表中获取所有类型为'table'的表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # 获取查询结果
    tables = cursor.fetchall()

   # 遍历所有表并显示内容
    for table in tables:
        
        # 表的名字
        table_name = table[0]
        print(f"Table: {table_name}")

        # 查询表的所有数据
        cursor.execute(f"SELECT * FROM {table_name};")
        # 从数据库中获取所有数据
        rows = cursor.fetchall()

        # 变量 每一行 的数据
        for row in rows:
            print(row)

    # 关闭数据库连接
    conn.close()

    #  execute方法用于执行SQL查询语句。
    #  f"SELECT * FROM {table_name};"是一个格式化字符串，
    #  用于生成SQL查询语句。{table_name}是一个占位符，会被实际表名替换。
    #  SELECT * FROM表示查询表中的所有字段。





# sqlite,创建表，
def sqlite_create_table(db_path):

    # 设置文件夹路径
    folder_path = db_path

    # 创建或连接到SQLite数据库
    db_path = 'filenames.db'
    conn = sqlite3.connect(db_path)

    # 创建一个cursor对象
    cursor = conn.cursor()

    # 创建一个表来存储文件名
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filenames (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            
        )
    ''')
    # ,  filename TEXT 
    # 提交事务
    conn.commit()

    # 关闭cursor和连接
    cursor.close()
    conn.close()

# 插入 新的 列
def sqlite_insert_column(db_path, column_name):

    # 创建或连接到SQLite数据库
    conn = sqlite3.connect(db_path)

    # 创建一个cursor对象
    cursor = conn.cursor()

    # 插入数据
    cursor.execute(f"ALTER TABLE filenames ADD COLUMN {column_name} TEXT;")

    # 提交事务
    conn.commit()

    # 关闭cursor和连接
    cursor.close()
    conn.close()

# 删除 列
def sqlite_delete_column(db_path, column_name):

    # 创建或连接到SQLite数据库
    conn = sqlite3.connect(db_path)

    # 创建一个cursor对象
    cursor = conn.cursor()

    # 插入数据
    cursor.execute(f"ALTER TABLE filenames DROP COLUMN {column_name};")

    # 提交事务
    conn.commit()

    # 关闭cursor和连接
    cursor.close()
    conn.close()

# 插入数据 到 表 内的 列
def sqlite_insert_data(db_path, column ,data):
    
    # 创建或连接到SQLite数据库
    conn = sqlite3.connect(db_path)

    # 创建一个cursor对象
    cursor = conn.cursor()

    # 插入数据
    cursor.execute("INSERT INTO filenames (filename) VALUES (?)", (data,))

    # 提交事务
    conn.commit()

    # 关闭cursor和连接
    cursor.close()
    conn.close()

# 插入，一行数据，到表
def insert_row_to_table(db_path, table_name, column_names, row_data):
    
    # 类型注解
    column_names: list[str]
    row_data: list[str]

    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:

        # 构建SQL插入语句（假设column_names和row_data的长度相同）
        columns_str = ', '.join(column_names)
        placeholders_str = ', '.join('?' * len(column_names))
        sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders_str});"

        # 执行SQL语句
        cursor.execute(sql, row_data)

        # 提交事务
        conn.commit()
        print("数据已成功插入.")
    except sqlite3.Error as e:

        print(f"发生错误: {e}")
        # 如果有错误，回滚事务
        conn.rollback()
    finally:

        # 关闭游标和连接
        cursor.close()
        conn.close()


# 删除sqlite除了列名，所有数据
def sqlite_delete_data(db_path):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM filenames")

    conn.commit()

    cursor.close()
    conn.close()

# sqlite 显示 所有列名
def sqlite_show_columns(db_path):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(filenames)")
    columns = cursor.fetchall()

    for column in columns:
        print(column)

    cursor.close
    conn.close()

# 删除 表
def sqlite_delete_table(db_path):

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE filenames")

    conn.commit()

    cursor.close()
    conn.close()

# 搜索文件，插入 表
def find_files(full_path,db_path3):

    # 获取文件名，不含 目录
    filename = os.path.basename(full_path)

    # 获取 文件的没有扩展名 部分
    fils_short = os.path.splitext(filename)[0]
    # 获取 扩展名
    extname = os.path.splitext(filename)[1]

    print("file name(no ext):", fils_short )

    # 判断 文件名 fils_short  是否有 -C
    if '-C' in fils_short :

        # 获取 文件名 部分
        fils_short  = fils_short.split('-C')[0]
        has_subtitle = 'y'
        print("file name:", fils_short )
    else:

        # 没有字幕
        has_subtitle = 'n'
        print("file name no -c")

    # 全路径
    print("full_path:", full_path)

    
    # 表的 列名
    column_names = ['filename', 'short_name','extname', 'has_subtitle', 'fullpath']
    # 表的 一行数据
    row_data = [filename, fils_short, extname, has_subtitle, full_path]
    print("row_data:", row_data)

    # 插入，一行数据
    # insert_row_to_table(db_path3,'filenames', column_names, row_data)

# 某一列 里 搜索字符串 
def search_string_in_column(db_path, table_name, column_name, target_string):
    
    # 连接到SQLite数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # 构建SQL查询语句
        sql = f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%{target_string}%';"

        # 执行查询
        cursor.execute(sql)

        # 获取所有匹配的结果行
        result_rows = cursor.fetchall()

        # 如果结果非空，则说明字符串存在于该列中
        if result_rows:
            print(f"找到'{target_string}'在'{table_name}.{column_name}'中的匹配项:")
            for row in result_rows:
                print(row)
            return True
        else:
            print(f"'{target_string}'未在'{table_name}.{column_name}'中找到.")
            return False
    except sqlite3.Error as e:
        print(f"发生错误: {e}")
        return None
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()


# 搜索mp4 文件
def find_mp4_files(directory):
    
    mp4_files = []
    
    for root, dirs, files in os.walk(directory):
        # 遍历 全路径
        for file in files:
            # 判断扩展名 
            if file.endswith('.mp4'):
                # 列表 添加，全路径
                mp4_files.append(os.path.join(root, file))
    
    return mp4_files


# mp4 存放 到 sqlite
def mp4_files_to_db():

    # mp4 search
    directory_to_search = input("请输入要搜索的文件夹路径：")
    mp4_list = find_mp4_files(directory_to_search)

    # 打印出找到的所有MP4文件路径
    for mp4_file in mp4_list:
        
        print(mp4_file)

        # 插入路径，到sqlite
        find_files(mp4_file,db_path2)

# end ~~~~~~~~~~~~~
    


# start ~~~~~~~~~~~~~~~
    



#获取py文件路径
# 获取当前脚本的完整路径
script_path = os.path.abspath(__file__)

# 获取当前脚本所在的目录
script_directory = os.path.dirname(script_path)

# db路径
db_path2 = script_directory + '\\filenames.db'

# 搜索文件夹 路径
folder_path = script_directory

# 删除全部数据，不含列名
# sqlite_delete_data(db_path2)


# 创建 表
# sqlite_create_table(db_path2)



# 插入 新的 列

# 表的 列名，
# column_names2 = ['filename', 'short_name','extname', 'has_subtitle', 'fullpath']

# # 遍历column_name2 
# for column_name in column_names2:
#     # 插入列名
#     sqlite_insert_column(db_path2,column_name)



# 删除列
# sqlite_delete_column(db_path2, "fullpath")

# 显示所有 列 名字
sqlite_show_columns(db_path2)

# 删除 表
# sqlite_delete_table(db_path2)

# 搜索文件 插入 表
# find_files(db_path2)



# 输入数字，选择不同 函数
switch_function = int(input("请输入数字，选择不同功能：\n1. 搜索文件名\n2.文件夹插入数据库\n"))

if switch_function == 1:

    # 搜索文件名
    # 搜索字符串 在 某一列
    # 'fullpath'
    strend = search_string_in_column(db_path2, "filenames", 'short_name',"sqlite")
    print("find str:",strend)

elif switch_function == 2:

    # 文件夹插入数据库
    # mp4文件 插入 sqlite
    mp4_files_to_db()

# 显示 全部表 的数据
dispaly_sqlite_all_tables(db_path2)