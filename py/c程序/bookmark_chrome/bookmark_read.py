# 获取chrome 书签，特定文件夹的 所有网址
import json
import os


# 读取 书签
def read_chrome_bookmarks(bookmarks_file_path,folder_name):

    # 读取书签文件
    with open(bookmarks_file_path, 'r', encoding='utf-8') as f:
        bookmarks_data = json.load(f)

    # 初始化一个空列表来存储网址和标题
    bookmarks = []

    # 解析书签数据，找到特定文件夹的书签
    for root, folders in bookmarks_data['roots'].items():

        if 'children' in folders:
            for folder in folders['children']:

                if folder['name'] == folder_name:
                    # 遍历文件夹内的书签
                    for bookmark in folder['children']:

                        if bookmark['type'] == 'url':

                            # 提取网址和标题
                            url = bookmark['url']
                            title = bookmark['name']
                            
                            # 显示 网址，标题
                            print(url,title)
                            # 将网址和标题添加到列表中
                            bookmarks.append({'url': url, 'title': title})

    # 返回值 网址和标题 的 列表
    return bookmarks

#  指定的网址 和 标题，保存json
def save_bookmarks_to_json(bookmarks, output_file_path):

    # 保存到JSON文件
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(bookmarks, outfile, ensure_ascii=False, indent=4)

# 使用示例
# Chrome 书签文件的路径
#读取 json内的chrome 路径
with open('proxy.json', 'r', encoding='utf-8') as f:
    bookmarks_data = json.load(f)

bookmarks_file_path = bookmarks_data['chrome_bookmarks_path']


bookmarks_file_path = os.path.normpath(bookmarks_file_path)
print(bookmarks_file_path)

folder_name = '2_19'  # 替换为您想要获取的书签文件夹名称
output_file_path = 'bookmarks.json'  # 输出文件路径

# 读取书签并获取特定文件夹的书签
bookmarks = read_chrome_bookmarks(bookmarks_file_path, folder_name)

# 保存书签到JSON文件
save_bookmarks_to_json(bookmarks, output_file_path)

os.system("pause")