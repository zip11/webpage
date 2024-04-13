import bencodepy

def get_tracker_url(torrent_file):

    with open(torrent_file, 'rb') as f:

        torrent_data = bencodepy.decode(f.read())
        
        # 获取 Tracker 地址列表
        trackers = torrent_data.get(b'announce-list', []) or [torrent_data.get(b'announce')]
        
        # 提取第一个 Tracker 地址
        tracker_url = trackers[0][0].decode() if trackers else None
        
        return tracker_url

# 主程序
def main():
    
    # 获取用户输入的种子文件路径
    torrent_file = input("请输入种子文件路径: ")
    
    tracker_url = get_tracker_url(torrent_file)
    
    if tracker_url:
        print("种子文件中的 Tracker 网址:", tracker_url)
    else:
        print("未找到 Tracker 网址")

if __name__ == "__main__":

    main()
