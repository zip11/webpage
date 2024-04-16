import os
import shutil

def organize_folders(input_folder):
    """整理文件夹"""

    # 创建目标文件夹路径
    target_folder = os.path.join(input_folder, "number")
    null_folder = os.path.join(target_folder, "null")

    # 创建目标文件夹和null文件夹
    create_folder(target_folder)
    create_folder(null_folder)

    # 遍历输入文件夹下的所有子文件夹
    for subdir in os.listdir(input_folder):

        # 获取子文件夹 的 完整路径
        subdir_path = os.path.join(input_folder, subdir)

        # 判断子文件夹是否是纯数字命名
        if subdir.isdigit():

            # 遍历数字命名的子文件夹，查找srt文件
            for root, dirs, files in os.walk(subdir_path):
                for file in files:

                    # 判断文件是否为srt文件
                    if file.endswith(('.srt', '.ass', '.vtt', '.ssa', '.txt', '.zip', '.rar', '.sub', '.idx', '.SRT', '.smi')):

                        # 移动srt文件到目标文件夹
                        print(f"Moving {file} to {target_folder}")
                        move_file(os.path.join(root, file), target_folder)

    # 移动已经移动了srt文件的空文件夹到null文件夹
    move_empty_folders(input_folder, null_folder)

def create_folder(folder):
    """创建文件夹"""
    if not os.path.exists(folder):
        os.makedirs(folder)

def move_file(source, destination):
    """移动文件"""
    shutil.move(source, destination)

def move_folder(source, destination):
    """移动文件夹"""
    shutil.move(source, destination)

def move_empty_folders(input_folder, null_folder):
    """移动空文件夹到null文件夹"""

    for subdir in os.listdir(input_folder):

        # 获取子文件夹的完整路径
        subdir_path = os.path.join(input_folder, subdir)

        # 判断子文件夹是否为空
        if os.path.isdir(subdir_path) and not os.listdir(subdir_path):

            # 移动空文件夹到null文件夹
            print(f"Moving empty folder {subdir} to {null_folder}")
            move_folder(subdir_path, null_folder)

# 判断 主函数
            
if __name__ == "__main__":

    # 输入文件夹路径
    input_folder = input("请输入文件夹路径: ")
    organize_folders(input_folder)
