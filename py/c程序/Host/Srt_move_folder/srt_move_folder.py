import os
import shutil

def get_prefix(filename):
    """获取文件名的前缀部分"""
    return filename.split('-')[0]

def create_folder(folder_path):
    """创建文件夹"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

def move_file(source_file, target_file):
    """移动文件"""
    shutil.move(source_file, target_file)
    print(f"Moved file '{source_file}' to folder '{os.path.dirname(target_file)}'")



def organize_srt_files(folder_path):
    """整理srt文件

    Args:
        folder_path (str): 包含srt文件的文件夹路径

    """
    # 遍历文件夹内的所有文件
    for filename in os.listdir(folder_path):

        # 判断文件是否是需要处理的格式
        if filename.endswith(('.srt', '.ass', '.vtt', '.ssa', '.txt', '.zip', '.rar', '.sub', '.idx', '.SRT', '.smi')):

            # 获取文件名前缀
            prefix = get_prefix(filename)
            # 创建目标文件夹路径
            target_folder = os.path.join(folder_path, prefix)

            # 创建目标文件夹
            create_folder(target_folder)

            # 源文件路径
            source_file = os.path.join(folder_path, filename)
            # 移动文件到目标文件夹
            move_file(source_file, target_folder)


# 主函数
if __name__ == "__main__":

    folder_path = input("输入 srt 文件夹")

    # 整理srt文件
    organize_srt_files(folder_path)
