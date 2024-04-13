import subprocess

# "fsm maker torrent,transmission    ,Windows"

tr_token = ""



# 程序主体
def main():

    # 用户输入文件路径
    file_path = input("请输入您想要创建种子的文件或文件夹路径：").strip()
    
    # Tracker网址设定为 "test"
    tracker_url = "https://connects.icu/Announce?passkey=" + tr_token
    # tracker_url2 = "https://nextpt.net/Announce?passkey=" + tr_token
    
    # 私有种子的标记
    private_flag = '--private'
    # 输出种子的文件名
    output_torrent = file_path + '.torrent'

    # 假设您的transmission-create命令在以下路径
    custom_path = 'D:\\Program Files\\Transmission\\transmission-create.exe'
    
    # 构造命令
    command = [
        custom_path, 
        '-o', output_torrent, 
        '-t', tracker_url,
        # '-t', tracker_url2,
        '-r', 'FSM',
        private_flag,
        file_path
    ]
    
    """
    -p: 表示生成私有种子，私有种子通常需要提供种子的 Tracker 地址，以便种子下载者能够连接到种子的 Tracker 服务器进行下载。

    -t: 指定 Tracker 地址。在这里，https://creditracker.net/Announce?passkey=xxx 是 Tracker 的地址，
        passkey 是一种身份验证方式，用于识别种子下载者的身份。xxx 是具体的 passkey，需要根据实际情况进行替换。
        
    -r: 指定种子的备注信息，通常可以用来标识种子所属的种子组织或者分类等信息。

    """    

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

    print("fsm maker torrent,transmission")
    main()