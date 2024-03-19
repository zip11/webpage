#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys

# 设置目标音频格式为Opus
audio_to_ext = "opus"

def find_media_files(folder_path):
    """
    搜索指定文件夹中的M4A文件。
    :param folder_path: 要搜索的文件夹路径
    :return: 包含找到的M4A文件名的列表
    """
    media_files = []
    for file_name in os.listdir(folder_path):
        # 检查文件扩展名是否为.m4a
        if file_name.endswith(".m4a"):
            media_files.append(file_name)
    return media_files

def convert_media_to_opus(file_list, folder_path):
    """
    将找到的M4A文件转换为Opus格式。
    :param file_list: 包含M4A文件名的列表
    :param folder_path: 包含M4A文件的文件夹路径
    """
    for media_file in file_list:
        # 分离文件名和扩展名
        base_name, extension = os.path.splitext(media_file)
        # 构造输出文件名
        output = base_name
        output_audio_name = output + "." + audio_to_ext

        # 构造完整的文件路径
        full_media_path = os.path.join(folder_path, media_file)
        full_audio_path = os.path.join(folder_path, output_audio_name)

        # 定义FFmpeg转换命令
        codec_command = 'ffmpeg -i "%s" -c:a libopus -vbr on -b:a 64k -ac 1 "%s"' % (full_media_path, full_audio_path)

        # 打印转换命令
        print('Running command:', codec_command)
        # 执行转换命令
        return_code = os.system(codec_command)

        # 检查转换是否成功
        if return_code == 0:
            # 删除原始M4A文件
            os.remove(full_media_path)
            print("Deleted:", media_file)
        else:
            print("Failed to convert:", media_file)

def main(folder_path):
    """
    主函数，执行M4A到Opus的转换流程。
    :param folder_path: 要搜索和转换文件的文件夹路径
    """
    print("M4A 转" + audio_to_ext + "，保持原始采样率，单声道，动态码率 VBR")
    print("py file:", folder_path)

    # 规范化文件夹路径
    source = os.path.normpath(folder_path)
    # 查找M4A文件
    media_files = find_media_files(source)
    # 打印找到的文件
    print('Media files found:', media_files)

    # 转换找到的媒体文件
    convert_media_to_opus(media_files, source)

    # 完成转换
    print("\n<<< 视频转音频完成 >>>")

if __name__ == "__main__":
    # 检查命令行参数数量
    if len(sys.argv) < 2:
        print("Usage: python script_name.py folder_path")
        sys.exit(1)
    
    # 获取文件夹路径参数
    folder_path = sys.argv[1]
    # 执行主函数
    main(folder_path)