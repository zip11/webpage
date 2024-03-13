import os
import subprocess
import sys
import re

def get_video_length(video_path):
    """
    使用 ffprobe 获取指定视频文件的时长（秒）。
    """
    command = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 \"{video_path}\""
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

    matches = re.search(r"(\d+\.\d+)", result.stdout)
    if matches:
        return float(matches.group(1))
    else:
        raise ValueError(f"无法从 ffprobe 输出中获取时长: {result.stdout}")

def execute_ffmpeg_command(command, output_file):
    """
    执行 FFmpeg 命令，并根据输出文件的大小决定是否保留该文件。
    """
    process = subprocess.run(command, shell=True, text=True)
    if process.returncode != 0 or (os.path.exists(output_file) and os.path.getsize(output_file) <= 1000):
        os.remove(output_file)
        return False
    return True

def convert_and_split_to_mp3(folder_path, segment_duration):
    """
    转换指定文件夹内所有 FLV 文件至 MP3，且根据给定时长分割 MP3 文件。
    """
    for video_file in os.listdir(folder_path):
        if video_file.endswith(".flv"):
            video_file_path = os.path.join(folder_path, video_file)
            video_length = get_video_length(video_file_path)
            base_name = os.path.splitext(video_file)[0]
            destination_folder = create_directory_for_audio(base_name, folder_path)

            segment_index = 1
            while (segment_duration * (segment_index - 1)) < video_length:
                audio_file_name = os.path.join(destination_folder, f"{base_name}_{segment_index:03}.mp3")
                start_time = segment_duration * (segment_index - 1)
                
                convert_command = (
                    f'ffmpeg -i "{video_file_path}" -vn -acodec libmp3lame -q:a 4 -ac 1 '
                    f'-ss {start_time} -t {segment_duration} "{audio_file_name}"'
                )

                success = execute_ffmpeg_command(convert_command, audio_file_name)
                if not success:
                    break
                
                segment_index += 1

def create_directory_for_audio(audio_name, source_path):
    """
    在指定源路径内为音频创建一个新的目录。
    """
    directory_path = os.path.join(source_path, audio_name)
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)
    return directory_path

# 实现命令行接口
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path to directory of flv files>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("The provided path is not a valid directory.")
        sys.exit(1)

    segment_duration = 600  # Segment duration set to 10 minutes (600 seconds)
    convert_and_split_to_mp3(folder_path, segment_duration)