#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys

# 设置目标音频格式为Opus
audio_to_ext = "opus"


# 获取exe程序 上一级 文件夹，flv文件转opus

def get_exe_directory():
    """
    获取当前可执行文件所在的文件夹的完整路径。
    """
    exe_path = sys.executable
    exe_directory = os.path.dirname(exe_path)
    return exe_directory


def find_media_files(folder_path):
    """
    搜索指定文件夹中的FLV文件。
    :param folder_path: 要搜索的文件夹路径
    :return: 包含找到的FLV文件名的列表
    """
    media_files = []

    for root, dirs, files in os.walk(folder_path):
        
        for file_name in files:

            # 检查文件扩展名是否为.flv
            if file_name.endswith(".flv"):
                media_files.append(os.path.join(root, file_name))

    return media_files

def convert_media_to_opus(file_list):
    """
    将找到的FLV文件转换为Opus格式。
    :param file_list: 包含FLV文件的列表
    """
    for media_file in file_list:

        # 分离文件名和扩展名
        base_name, extension = os.path.splitext(media_file)
        # 构造输出文件名
        output = base_name
        output_audio_name = output + "." + audio_to_ext

        # 定义FFmpeg转换命令
        codec_command = f'ffmpeg -i "{media_file}" -c:a libopus -vbr on -b:a 64k -ac 1 "{output_audio_name}"'
        # 打印转换命令
        print('Running command:', codec_command)
        # 执行转换命令
        return_code = os.system(codec_command)

        # 检查转换是否成功
        if return_code == 0:

            # 删除原始FLV文件
            os.remove(media_file)
            print("Deleted:", media_file)

        else:
            print("Failed to convert:", media_file)



def main():
    """
    主函数，执行FLV到Opus的转换流程。
    """
    # 获取py文件的上一级文件夹路径
    # script_path = os.path.abspath(__file__)
    # parent_folder = os.path.dirname(script_path)

    # 获取 exe 所在文件夹
    # parent_folder = get_exe_directory

    parent_folder = input("请输入文件夹路径:")

    print("Parent folder:", parent_folder)
    # os.system('pause')


    # 获取上一级文件夹的子文件夹
    sub_folders = [os.path.join(parent_folder, name) for name in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, name))]
    # 打印子文件夹列表
    print("Sub folders:", sub_folders)

    # 逐个搜索和转换FLV文件
    for folder in sub_folders:

        # 查找FLV文件
        media_files = find_media_files(folder)
        # 打印找到的文件
        print('Media files found in folder', folder, ':', media_files)
        # 转换找到的媒体文件
        convert_media_to_opus(media_files)
        
    # 完成转换
    print("\n<<< 视频转音频完成 >>>")

    os.system('pause')

if __name__ == "__main__":
    main()
