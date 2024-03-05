import os
import subprocess

def convert_to_mp3(m4a_path):

    # 获取M4A文件名（不含后缀名）
    m4a_name = os.path.splitext(os.path.basename(m4a_path))[0]
    
    # 获取M4A所在文件夹路径
    m4a_dir = os.path.dirname(m4a_path)

    # 创建以MP3文件名为名称的文件夹
    # mp3_dir = os.path.join(m4a_dir, f"{m4a_name}_mp3")
    # os.makedirs(mp3_dir, exist_ok=True)
    
    mp3_dir = m4a_dir

    # 使用FFmpeg进行M4A转MP3
    mp3_path = os.path.join(mp3_dir, f"{m4a_name}.mp3")
    command = f'ffmpeg -i "{m4a_path}" -codec:a libmp3lame  -q:a 4 -ac 1 "{mp3_path}"'
    subprocess.run(command, shell=True)
    
    return mp3_path

def split_mp3(mp3_path):

    # 获取MP3文件名（不含后缀名）
    mp3_name = os.path.splitext(os.path.basename(mp3_path))[0]
    
    # 获取MP3所在文件夹路径
    mp3_dir = os.path.dirname(mp3_path)

    # 创建存放分割MP3的文件夹
    output_dir = os.path.join(mp3_dir, f"{mp3_name}")
    os.makedirs(output_dir, exist_ok=True)

    # 使用FFmpeg进行分割
    command = f'ffmpeg -i "{mp3_path}" -f segment -segment_time 600 -c copy "{output_dir}/{mp3_name}_%03d.mp3"'
    subprocess.run(command, shell=True)

if __name__ == "__main__":

    # 从键盘输入M4A文件路径
    m4a_path = input("请输入M4A文件路径：")

    # 转换为MP3格式并获取MP3路径
    mp3_path = convert_to_mp3(m4a_path)

    # 调用函数进行分割
    split_mp3(mp3_path)
