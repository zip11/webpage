#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os

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
        '-cq', '33',  # 控制质量因子（数值越低质量越好）
        '-b:v', '3M',  # 平均比特率
        '-c:a', 'copy',  # 音频复制，不转码
        output_file  # 输出文件
    ]

    # 执行ffmpeg命令
    subprocess.run(ffmpeg_command)
    print(f"转码完成：{output_file}")

if __name__ == '__main__':
    input_path = input("请输入视频文件路径：")

    transcode_video(input_path)