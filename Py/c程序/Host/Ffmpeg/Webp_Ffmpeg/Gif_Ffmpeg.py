import subprocess

def extract_gif(input_video, output_gif, start_time, end_time):

    # 格式化开始时间和结束时间为ffmpeg接受的格式（hh:mm:ss）
    start_time_formatted = '{:02d}:{:02d}:{:02d}'.format(start_time // 3600, (start_time % 3600) // 60, start_time % 60)

    # start_time除以3600得到小时，然后取余数得到分钟，
    # 最后取余数得到秒，并将它们格式化为一个字符串，例如"00:00:00"。
    
    end_time_formatted = '{:02d}:{:02d}:{:02d}'.format(end_time // 3600, (end_time % 3600) // 60, end_time % 60)
    
    # 构建ffmpeg命令
    ffmpeg_command = [
        'ffmpeg',
        '-ss', start_time_formatted,  # 开始时间
        '-i', input_video,
        '-to', end_time_formatted,    # 结束时间
        '-vf', 'fps=10,scale=320:-1:flags=lanczos',
        '-c:v', 'webp',
        output_gif
    ]
    
    # 执行ffmpeg命令
    subprocess.run(ffmpeg_command)

if __name__ == "__main__":

    input_video = input("请输入视频文件路径：")
    output_gif = input("请输入输出WebP 文件路径：")

    start_minutes = int(input("请输入开始分钟数："))
    start_seconds = int(input("请输入开始秒数："))

    end_minutes = int(input("请输入结束分钟数："))
    end_seconds = int(input("请输入结束秒数："))
    
    # 开始时间和结束时间转换为秒数
    start_time = start_minutes * 60 + start_seconds
    end_time = end_minutes * 60 + end_seconds
    
    # 调用函数提取GIF
    extract_gif(input_video, output_gif, start_time, end_time)
