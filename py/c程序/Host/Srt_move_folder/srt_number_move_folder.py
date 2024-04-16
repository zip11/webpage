import os
import shutil

def count_subtitles(folder):
    """统计文件夹下的字幕文件数量（支持多种格式）"""
    
    # 支持的字幕文件格式
    supported_formats = ('.srt', '.ass', '.vtt', '.ssa', '.txt', '.zip', '.rar', '.sub', '.idx', '.SRT', '.smi')
    
    # 统计各种格式的字幕文件数量
    total_count = 0
    for format in supported_formats:
        files = [f for f in os.listdir(folder) if f.endswith(format)]
        total_count += len(files)
    
    return total_count



def move_subtitles(source_folder, destination_folder):
    """移动字幕文件到目标文件夹"""

    # 遍历源文件夹中的字幕文件，逐个移动到目标文件夹
    for filename in os.listdir(source_folder):

        if filename.endswith(('.srt', '.ass', '.vtt', '.ssa', '.txt', '.zip', '.rar', '.sub', '.idx', '.SRT', '.smi')):

            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)

            shutil.move(source_file, destination_file)

def organize_subtitles(input_folder):
    """整理文件夹下的子文件夹中的字幕文件"""

    # 创建目标文件夹
    duo_folder = os.path.join(input_folder, 'duo')
    shao_folder = os.path.join(input_folder, 'shao')
    os.makedirs(duo_folder, exist_ok=True)
    os.makedirs(shao_folder, exist_ok=True)
    
    # 遍历子文件夹
    subfolders = [f for f in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, f))]

    for subfolder in subfolders:
    
        subfolder_path = os.path.join(input_folder, subfolder)
        total_count = count_subtitles(subfolder_path)
    
        if total_count > 10:
            destination_folder = duo_folder
        else:
            destination_folder = shao_folder
        move_subtitles(subfolder_path, destination_folder)

# 测试代码
if __name__ == "__main__":

    input_folder = input("请输入文件夹路径: ")
    organize_subtitles(input_folder)
