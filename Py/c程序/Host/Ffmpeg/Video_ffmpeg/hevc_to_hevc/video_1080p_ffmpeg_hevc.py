import subprocess
import os

def get_conversion_option():
    """
    提供转换选项：是否只转换视频的开头6分钟。
    """
    print("请选择转换选项：")
    print("1. 转换整个视频")
    print("2. 转换视频的开头6分钟")
    conversion_option = input("请选择一个选项 (按回车键选择默认值 [1. 转换整个视频]): ") or '1'

    if conversion_option == '1':
        return False
    elif conversion_option == '2':
        return True
    else:
        print("无效的选择，将转换整个视频.")
        return False

def transcode_video(input_file, convert_first_three_minutes=False):
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
        '-c:v', 'hevc_cuvid',  # 使用NVIDIA的硬件解码器进行H.264解码
        '-i', input_file,  # 输入文件
    ]

    # 如果选择转换视频的开头三分钟，则添加相应的选项
    if convert_first_three_minutes:
        ffmpeg_command.extend(['-t', '00:06:00'])

    # 继续构建转码命令
    ffmpeg_command.extend([
        # '-vf', 'scale_cuda=1920:1080',  # 使用NVIDIA硬件加速进行分辨率缩放
        '-c:v', 'hevc_nvenc',  # 使用NVIDIA的硬件编码器进行HEVC编码
        '-preset', 'slow',  # 编码预设，较慢的速度通常意味着更好的压缩，提高输出质量
        '-rc', 'vbr',  # 可变比特率控制
        '-cq', '28',  # 控制质量因子（数值越低质量越好）
        '-b:v', '3M',  # 平均比特率
        '-c:a', 'copy',  # 音频复制，不转码
        output_file  # 输出文件
    ])

    # 执行ffmpeg命令
    subprocess.run(ffmpeg_command)
    print(f"转码完成：{output_file}")

if __name__ == '__main__':

    print("hevc to hevc")
    
    input_path = input("请输入视频文件路径：")
    
    convert_first_three_minutes = get_conversion_option()

    transcode_video(input_path, convert_first_three_minutes)
