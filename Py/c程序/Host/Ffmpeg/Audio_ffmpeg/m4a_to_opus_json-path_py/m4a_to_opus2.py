import os
import subprocess
import json
import sys

def m4a_to_opus(folder_path):
    # 获取所有 M4A 文件
    m4a_files = [file for file in os.listdir(folder_path) if file.endswith('.m4a')]
    
    for m4a_file in m4a_files:
        input_file = os.path.join(folder_path, m4a_file)
        output_file = os.path.join(folder_path, os.path.splitext(m4a_file)[0] + '.opus')

        # 使用 ffmpeg 进行转换
        ffmpeg_command = f'ffmpeg -i "{input_file}" -vn -c:a libopus -vbr on -b:a 64k -ac 1 "{output_file}"'
        process = subprocess.Popen(ffmpeg_command, shell=True)
        process.wait()

        if process.returncode == 0:
            print(f"转换完成: {output_file}")
            # 删除 M4A 文件
            os.remove(input_file)
            print(f"已删除: {input_file}")
        else:
            print(f"转换失败: {input_file}")

def get_folder_path():
    # 获取当前脚本文件的文件夹路径
    return os.path.dirname(os.path.abspath(__file__))

def get_json_file_path(folder_path):
    # 拼接文件夹路径和 JSON 文件名
    return os.path.join(folder_path, "file_paths.json")


    
def get_folder_paths_from_json(json_file_path):

    with open(json_file_path, encoding='utf-8') as f:
        data = json.load(f)
        return data.get("filePaths", [])

def main():

    # 获取当前脚本文件的文件夹路径
    folder_path = get_folder_path()
    print("当前文件夹路径:", folder_path)

    # 获取 JSON 文件路径
    json_file_path = get_json_file_path(folder_path)
    print("JSON 文件路径:", json_file_path)

    # 从 JSON 文件中读取文件夹路径
    folder_path_from_json = get_folder_paths_from_json(json_file_path)

    # 判断 路径 存在
    if folder_path_from_json is None:
        print("无效的 JSON 文件或未找到文件夹路径。")
        return

    print("FLV 和 TS 转 OPUS，保持原始采样率，单声道，动态码率 VBR")
    print("文件夹路径:", folder_path_from_json)

    # 遍历 json_file_path
    for folder_path in folder_path_from_json:

        # 进行音频转换
        m4a_to_opus(folder_path)

    print("\n<<< 视频转音频完成 >>>")

if __name__ == "__main__":
    main()
