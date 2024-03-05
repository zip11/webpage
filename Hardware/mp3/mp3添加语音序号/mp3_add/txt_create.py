import os

# python，批量新建txt文件，py文件的文件的目录，新建名字是 txt 的文件夹,目录里面存放txt，
# 文件名是数字序号，例如000.txt,内容是文件名（例如 000），生成到数量到100.txt

# 设置文件夹名称和文本文件的起始序号
folder_name = 'txt'
start序号 = 0
end序号 = 100

# 创建文件夹
txt_folder_path = os.path.join(os.getcwd(), folder_name)
os.makedirs(txt_folder_path, exist_ok=True)

# 批量创建文本文件
for i in range(start序号, end序号 + 1):

    file_name = f'{i:03d}.txt'  
    # 使用03d格式化字符串，确保序号是三位数
    
    file_path = os.path.join(txt_folder_path, file_name)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(file_name[:-4])  
        # 写入内容，不包括.txt扩展名

print(f'Created {end序号 - start序号} text files in {txt_folder_path}')