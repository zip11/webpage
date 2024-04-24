import json

def read_json(filename):

    # 读取JSON文件并加载内容
    with open(filename, 'r') as file:
        data = json.load(file)
    
    # 获取contentArray列表并返回
    content_array = data.get('contentArray', [])
    return content_array

# 示例用法
filename = 'content.json'

content_list = read_json(filename)

print(content_list)
