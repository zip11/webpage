#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 使用NVIDIA硬件加速进行视频转码的ffmpeg Python脚本

import os
import subprocess

def transcode_video(input_path):
    """
    使用NVIDIA硬件加速将视频转码为H.264格式，采用VBR（可变比特率）
    """
    # 输出文件路径
    output_path = os.path.splitext(input_path)[0] + '_transcoded.mp4'
    
    # 构建ffmpeg命令
    cmd = [
       'ffmpeg',
        '-hwaccel', 'cuda',                   # 启用CUDA硬件加速
        '-hwaccel_output_format', 'cuda',     # 指定硬件加速的输出格式
        '-c:v', 'h264_cuvid',                 # 使用NVIDIA的硬件解码器进行解码
        '-i', input_path,                     # 输入文件路径
        '-t', '00:05:00',                     # 只处理前5分钟的视频
        '-vf', 'scale_cuda=1280:720',         # 使用NVIDIA硬件加速缩放视频分辨率到1280x720
        # ... 其他选项保持不变 ...
        '-c:v', 'h264_nvenc',         # 设置视频编解码器为NVIDIA的H.264
        '-rc', 'vbr',                 # 设置码率控制为VBR
        '-cq', '19',                  # 控制质量因子（数值越低质量越好）
        '-b:v', '5M',                 # 平均比特率
        '-maxrate', '10M',            # 最大比特率
        '-bufsize', '10M',            # 缓冲区大小
        '-c:a', 'copy',               # 复制音频流，不进行转码
        output_path                   # 输出文件路径
    ]
    
    # 执行ffmpeg命令
    subprocess.run(cmd)

if __name__ == '__main__':
    # 获取用户输入的视频文件路径
    video_path = input("请输入视频文件的路径: ")
    # 检查文件是否存在
    if os.path.isfile(video_path):
        transcode_video(video_path)
    else:
        print("文件不存在，请检查路径是否正确。")