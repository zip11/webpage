import os
import subprocess

def split_mp3(mp3_path):

    # 获取MP3文件名（不含后缀名）
    mp3_name = os.path.splitext(os.path.basename(mp3_path))[0]
    
    # 创建以MP3文件名为名称的文件夹
    output_dir = mp3_name
    os.makedirs(output_dir, exist_ok=True)
    
    # 使用FFmpeg进行分割
    command = f'ffmpeg -i "{mp3_path}" -f segment -segment_time 600 -c copy "{output_dir}/{mp3_name}_%03d.mp3"'
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    
    # 从键盘输入MP3路径
    mp3_path = input("请输入MP3文件路径：")

    # 调用函数进行分割
    split_mp3(mp3_path)
