from dottorrent import Torrent
import sys
import os

tr_token = ""


def main():
    # 提示用户输入文件路径
    file_path = input("请输入文件或目录的路径：")
    if not os.path.exists(file_path):
        print("文件或目录不存在，请检查路径。")
        sys.exit(1)
    
    # 默认的两个Tracker
    
    tracker_url = "https://connects.icu/Announce?passkey=" + tr_token
    # tracker_url2 = "https://nextpt.net/Announce?passkey=" + tr_token
    
    trackers = [
        tracker_url,
        # tracker_url2
    ]
    
    # 创建Torrent对象,分块大小 2mb
    torrent = Torrent(file_path, trackers=trackers, piece_size=2048*1024 ,private=True, include_md5=True)
    
    # 生成种子文件
    torrent.generate()
    
    # 保存种子文件
    output_filename = os.path.join(os.path.dirname(file_path), os.path.basename(file_path) + '.torrent')
    with open(output_filename, 'wb') as f:
        torrent.save(f)
    
    print(f"种子文件已保存为：{output_filename}")

if __name__ == "__main__":
    main()