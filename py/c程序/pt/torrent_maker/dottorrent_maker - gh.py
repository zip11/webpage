from dottorrent import Torrent
import sys
import os

def main():
    # 提示用户输入文件路径
    file_path = input("请输入文件或目录的路径：")
    if not os.path.exists(file_path):
        print("文件或目录不存在，请检查路径。")
        sys.exit(1)
    
    # 默认的两个Tracker
    trackers = [
        'http://tracker1.example.com:80/announce',
        'http://tracker2.example.com:80/announce'
    ]
    
    # 创建Torrent对象
    torrent = Torrent(file_path, trackers=trackers, private=True, include_md5=True)
    
    # 生成种子文件
    torrent.generate()
    
    # 保存种子文件
    output_filename = os.path.join(os.path.dirname(file_path), os.path.basename(file_path) + '.torrent')
    with open(output_filename, 'wb') as f:
        torrent.save(f)
    
    print(f"种子文件已保存为：{output_filename}")

if __name__ == "__main__":
    main()