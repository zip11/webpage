import os
import shutil

def create_number_folder(input_folder):

    # 创建目标文件夹
    target_folder = os.path.join(input_folder, "number")

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

def move_srt_files(input_folder):

    # 遍历文件夹下的文件
    for filename in os.listdir(input_folder):

        #
        file_path = os.path.join(input_folder, filename)

        # 判断 srt 文件
        if os.path.isfile(file_path) and filename.endswith(('.srt', '.ass', '.vtt', '.ssa', '.txt', '.zip', '.rar', '.sub', '.idx', '.SRT', '.smi')):

            # 获取文件名前缀
            prefix = filename.split('_')[0]
            # 目标文件夹路径
            destination_folder = os.path.join(input_folder, "number", prefix)

            # 移动文件到目标文件夹
            shutil.move(file_path, destination_folder)

# 测试代码
def main():

    input_folder = input("请输入文件夹路径: ")

    #   创建目标文件夹
    create_number_folder(input_folder)

    # 移动srt文件到目标文件夹
    move_srt_files(input_folder)

if __name__ == "__main__":

    main()
