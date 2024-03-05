import os
import subprocess
import glob
import re

# bilibili
# 直播mp3_10分钟一个文件，mp3文件 头，添加数字序号mp3，
# 每次运行，处理一个文件夹

# mp3下一首，比快进更快 ，音频太长，快进太慢

# 获取 直播 MP3，文件列表
def find_mp3_files_by_pattern(folder_path):

    """
    在指定文件夹及其子文件夹中搜索文件名末尾是数字的MP3文件。

    :param folder_path: 要搜索的文件夹路径
    :return: 文件路径列表
    """
    # 使用glob.glob()的recursive参数来递归搜索MP3文件
    mp3_files = glob.glob(os.path.join(folder_path, '**', '*.mp3'), recursive=True)
    return mp3_files

#  拼接 两个MP3文件
def concatenate_mp3_files(input_file1, input_file2, output_file,vbr_quality=0):

    """
    使用ffmpeg拼接两个MP3文件。

    :param input_file1: 第一个MP3文件的路径
    :param input_file2: 第二个MP3文件的路径
    :param output_file: 输出文件的路径
    """

    # 构建ffmpeg命令
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_file1,
        '-i', input_file2,
        "-filter_complex", "concat=n=2:v=0:a=1",
        "-c:a", "libmp3lame",
        "-q:a", str(vbr_quality), 
        "-ar", "48000", 
        output_file
    ]

    # ar 采样率 48khz， vbr 压缩质量 4
    
    # 运行ffmpeg命令
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f'Files have been combined into {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')

# 生成 纯数字 mp3 文件名
def get_new_mp3_path(file_path):


    """
    从给定的文件路径中提取末尾的纯数字，并拼接成新的MP3文件路径。

    :param file_path: 原始文件路径
    :return: 新的MP3文件路径
    """

    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # 使用正则表达式从文件名中匹配末尾的纯数字
    match = re.search(r'(\d+)(?=\.mp3)', os.path.basename(file_path))

    if match:
        
        # 提取数字部分
        number = match.group(1)

        # 拼接新的文件路径，mp3路径
        new_file_path = os.path.join(script_dir,'number', f"{number}.mp3")
        
        return new_file_path
    
    else:
        # 如果没有匹配到数字，返回None
        return None
    

# ~~~~~~start~~~~~~~~
    
print("start,number.mp3 + *.mp3,mix-mp3")



# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.realpath(__file__))
print(f'Current script directory: {script_dir}\n')

# 搜索mp3文件夹
search_mp3_folder = os.path.join(script_dir, 'input')
print(f'Searching for MP3 files in: {search_mp3_folder}\n')



# ~~~~~~~~~
# 在当前脚本所在目录及其子目录中搜索MP3文件
mp3_files = find_mp3_files_by_pattern(search_mp3_folder, )
print(f'Found {len(mp3_files)} MP3 files:{mp3_files}\n')


# 新建  mix 子文件夹 ~~开始~~~~~~~~~~~

# mp3_files[0] 获取文件的目录
mp3_input_dir = os.path.dirname(mp3_files[0])
# 获取 MP3 最后一个 目录
mp3_input_dir = os.path.basename(mp3_input_dir)
# 生成 mix 目录
mp3_mix_dir = os.path.join(script_dir, 'mix', mp3_input_dir)

# 判断 目录 是否存在
if not os.path.exists(mp3_mix_dir):
    # 创建 文件夹
    os.makedirs(mp3_mix_dir, exist_ok=True)
    print(f'Create directory: {mp3_mix_dir}\n')

# end~~~~~~~
    

# 遍历 mp3 文件，第二个文件，包含数字序号
for mp3_file in mp3_files:

    print(f'mp3_file---------: {mp3_file}\n')
    
    # mp3，第一个文件，序号文件 ，只有数字
    first_mp3 = get_new_mp3_path(mp3_file)
    print(f'first_mp3: {first_mp3}\n')

    # 获取 数字mp3，文件名
    first_mp3_name = os.path.basename(first_mp3)
    print(f'first_mp3_name: {first_mp3_name}\n')

    # 获取 纯文件名 ，是 含汉字mp3
    mp3_file_name = os.path.basename(mp3_file)
    print(f'mp3_file_name: {mp3_file_name}\n')



    # ~~~~~~~ 拼接mp3 开始~~~~~~~~~~~~~~~~

    # 判断 mp3_file 里面 含有 first_mp3，并且 mp3_file 不等于 first_mp3
    if mp3_file_name != first_mp3_name and first_mp3_name in mp3_file_name:
        
        #  拼接 序号 文件名 mp3

        print(f'first_mp3: {first_mp3}  \n  mp3_file: {mp3_file}\n')

        # 获取mp3 文件名，无扩展名
        output_file_name = mp3_file_name
        # mix-mp3，文件名
        output_file = os.path.join(mp3_mix_dir, output_file_name)

        
        # 输出 带 数字序号，
        print(f'output_file: {output_file}\n')

        # 生成新 ，MP3文件
        concatenate_mp3_files(first_mp3, mp3_file, output_file)

