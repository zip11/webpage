import os
import shutil

def move_empty_folders(input_folder, output_folder):
    """移动空文件夹到指定目录"""

    # 创建目标文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取输入文件夹中的所有子文件夹
    subfolders = [f for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))]

    # 遍历子文件夹
    for subfolder in subfolders:

        subfolder_path = os.path.join(input_folder, subfolder)
        
        # 如果子文件夹为空，则移动到目标文件夹
        if not os.listdir(subfolder_path):
            shutil.move(subfolder_path, output_folder)

# 输入文件夹路径
input_folder = input('请输入文件夹路径: ')

# 输出文件夹路径
output_folder = os.path.join(input_folder, 'null')

# 创建 null 文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 移动空文件夹
move_empty_folders(input_folder, output_folder)
