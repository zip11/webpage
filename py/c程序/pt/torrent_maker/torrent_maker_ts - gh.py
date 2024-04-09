import subprocess

# 程序主体
def main():

    # 用户输入文件路径
    file_path = input("请输入您想要创建种子的文件或文件夹路径：").strip()
    
    # Tracker网址设定为 "test"
    tracker_url = "http://your.tracker.url:port/announce"
    
    # 私有种子的标记
    private_flag = '--private'
    # 输出种子的文件名
    output_torrent = file_path + '.torrent'

    # 假设您的transmission-create命令在以下路径
    custom_path = 'C:\\Program Files\\Transmission\\transmission-create.exe'
    
    # 构造命令
    command = [
        custom_path, 
        '-o', output_torrent, 
        '-t', tracker_url,
        private_flag,
        file_path
    ]
    
    # 执行命令
    try:
        subprocess.run(command, check=True)
        print(f'种子文件已创建: {output_torrent}')
    except subprocess.CalledProcessError as e:
        print(f"生成种子时遇到错误: {e}")
    except FileNotFoundError:
        print("找不到transmission-create工具，请确保它已被安装并且添加到了环境变量。")

# 主逻辑判断
if __name__ == "__main__":

    main()