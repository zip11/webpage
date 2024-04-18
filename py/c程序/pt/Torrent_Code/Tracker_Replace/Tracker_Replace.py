import bencodepy

def replace_tracker(torrent_file, new_tracker_url):

    # 打开种子文件并解析
    with open(torrent_file, 'rb') as f:
        torrent_data = bencodepy.decode(f.read())

    # 替换 Tracker 地址
    if b'announce-list' in torrent_data:

        # 多个 Tracker 地址的情况
        for i, tracker_list in enumerate(torrent_data[b'announce-list']):
            for j, tracker in enumerate(tracker_list):
                torrent_data[b'announce-list'][i][j] = new_tracker_url.encode()
                
    elif b'announce' in torrent_data:

        # 单个 Tracker 地址的情况
        torrent_data[b'announce'] = new_tracker_url.encode()

    # 保存修改后的种子文件
    with open(torrent_file, 'wb') as f:
        f.write(bencodepy.encode(torrent_data))

# 主程序
def main():

    # 获取用户输入的种子文件路径和新的 Tracker 网址
    torrent_file = input("请输入种子文件路径: ")
    new_tracker_url = input("请输入新的 Tracker 网址: ")

    # 调用函数替换 Tracker 网址
    replace_tracker(torrent_file, new_tracker_url)
    print("种子文件的 Tracker 网址已成功替换为:", new_tracker_url)

if __name__ == "__main__":
    main()
