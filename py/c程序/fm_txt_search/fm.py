# 搜索 txt指定字符串 ，的网址
def search_string_in_file(file_path, search_string):
    
    line_number = 0

    fmlist = []

    with open(file_path, 'r', encoding='utf-8') as file:
    
        for line in file:
    
            line_number += 1
    
            if search_string in line:

                print(f'在第 {line_number} 行找到 "{search_string}": {line.strip()}')
                # line.strip() 是 Python 中的一个字符串方法，用于去除字符串中的空白字符（包括空格、制表符和换行符）。
                # 这个方法通常用于从文件或其他文本数据中读取数据时，去除每行末尾的换行符或其他空白字符。
                
                fmlist.append(line.strip())
    
    return fmlist

# 创建m3u
def txt_to_m3u(file_path, fm_list):

    # 打开文件
    with open('radio.m3u', 'w', encoding='utf-8') as file:
        
        # 文件头 添加
        file.write('#EXTM3U\n')

        # 添加 音频文件
        for fm in fm_list:

            # 分割 名字 和 网址
            fg_fm = fm.split(',')

            # 音频 名字
            file.write(f'#EXTINF:-1,{fg_fm[0]}\n')

            #  音频 路径
            file.write(f'{fg_fm[1]}\n')
    
    print('创建m3u成功')


#  st ~~~~~~~~~~~~~~~~
import os

# 获取当前脚本所在目录
script_directory = os.path.dirname(os.path.abspath(__file__))

print(f"当前脚本所在目录： {script_directory}")


# fm-txt，拼接 全路径
file_path = os.path.join(script_directory, 'radio.txt')
search_string = '武汉'

# 搜索txt，字符串
m3u = search_string_in_file(file_path, search_string)

# m3u 全路径
m3u_file_path = os.path.join(script_directory, 'radio.m3u')
# 创建 m3u
txt_to_m3u(m3u_file_path, m3u)