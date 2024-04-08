#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
# print
import sys
import time



def transcode_video(input_file):
    """
    使用NVIDIA RTX 30系列显卡硬件加速将视频文件转码为HEVC格式。
    实现硬件解码H.264，硬件缩放到1280x720，硬件编码为HEVC，音频不变。
    输出为MP4格式，并将输出视频的名称设置为输入视频名称后加上"_hevc"。
    """
    # 输出文件路径，添加"_hevc"后缀
    output_file = os.path.splitext(input_file)[0] + '_hevc.mp4'
    
    # 构建ffmpeg命令行
    ffmpeg_command = [
        'ffmpeg',
        '-hwaccel', 'cuda',  # 启用CUDA硬件加速
        '-hwaccel_output_format', 'cuda',  # 指定硬件加速的输出格式
        '-c:v', 'h264_cuvid',  # 使用NVIDIA的硬件解码器进行H.264解码
        '-i', input_file,  # 输入文件
        # '-t', '00:05:00',                     # 只处理前5分钟的视频
        '-vf', 'scale_cuda=1280:720',  # 使用NVIDIA硬件加速进行分辨率缩放
        '-c:v', 'hevc_nvenc',  # 使用NVIDIA的硬件编码器进行HEVC编码
        '-preset', 'slow',  # 编码预设，较慢的速度通常意味着更好的压缩，提高输出质量
        '-rc', 'vbr',  # 可变比特率控制
        '-cq', '28',  # 控制质量因子（数值越低质量越好）
        '-b:v', '3M',  # 平均比特率
        "-bf", "4", # 设置B帧数量
        "-b_ref_mode", "2", # 设置B帧参考模式
        "-tier", "high", # 设置编码档次
        '-rc-lookahead' ,"40",  # 设置前瞻帧数
        '-spatial-aq', "1",  # 开启空间自适应量化
        '-temporal-aq', "1",  # 开启时间自适应量化
        '-c:a', 'copy',  # 音频复制，不转码
        output_file  # 输出文件
    ]

    print(f"开始转码：{input_file}")

    # 使用Popen代替run，并设置stderr为STDOUT，以便可以获取FFmpeg的进度信息
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

    # 实时读取输出信息
    while True:
        
        # 读取一行输出信息
        output = process.stdout.readline()

        # 检查是否已经完成转码
        if not output and process.poll() is not None:
            break
        
        # 检查是否已经完成转码
        if output:
            
            # 去除换行符
            word = output.strip()

            # 判断是否为进度信息
            if "speed" in word:
                
                # 覆盖显示 
                sys.stdout.write(f"\r\033[K{word}")
                sys.stdout.flush()
                # time.sleep(1)  # 模拟延迟
            else: 
                # 打印实时信息
                print(output.strip(), flush=True) 

    # 检查转码是否成功
    if process.returncode != 0:

        # 转码失败
        print(f"转码失败：{input_file}")
        return False
    else:
        # 转码成功
        print(f"转码完成：{output_file}")
        return True
    
def find_and_transcode_gg_folder(root_path):
    """
    在给定的根目录下找到所有名为'gg'的子目录，
    并转码其中的所有视频文件，若转码成功则删除源视频文件。
    """
    # 视频文件的扩展名列表
    VIDEO_EXTENSIONS = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')

    for dirpath, dirnames, filenames in os.walk(root_path):

        # 只处理名为'gg'的文件夹
        # if os.path.basename(dirpath) == 'g':

            # 遍历文件夹中的所有文件
            for filename in filenames:

                # 文件名不包含 hevc 字符串
                if 'hevc' not in filename.lower():

                    # 获取文件完整路径
                    file_path = os.path.join(dirpath, filename)

                    # 判断 是否为视频文件
                    if file_path.lower().endswith(VIDEO_EXTENSIONS):
                        
                        # 对视频文件进行转码
                        if transcode_video(file_path):

                            # 若转码成功，删除源文件
                            os.remove(file_path)
                            print(f"已删除源视频文件：{file_path}")

if __name__ == '__main__':

    input_path = input("请输入根目录路径：")
    
    # 检查路径是否存在
    find_and_transcode_gg_folder(input_path)