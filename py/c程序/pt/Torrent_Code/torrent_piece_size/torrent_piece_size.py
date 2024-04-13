import bencodepy
import sys
import os

def get_torrent_piece_size(torrent_path):

    try:

        # 读取种子文件
        with open(torrent_path, 'rb') as f:
            torrent_data = f.read()

        # 解码种子文件内容
        torrent_dict = bencodepy.decode(torrent_data)

        # 提取info部分
        info = torrent_dict[b'info']

        # 获取分块大小
        piece_length = info.get(b'piece length', None)

        if piece_length is not None:
            piece_length_kb = piece_length // 1024
            return piece_length_kb
        else:
            return "分块大小未指定，可能是多文件种子。"
    except Exception as e:
        return f"获取分块大小时发生错误：{e}"

def main():

    # 提示用户输入种子文件路径
    torrent_path = input("请输入种子文件(.torrent)的路径：")

    if not os.path.isfile(torrent_path):
        print("文件不存在，请检查路径。")
        sys.exit(1)
    
    # 获取分块大小
    piece_size = get_torrent_piece_size(torrent_path)
    print(f"种子文件的分块大小为：{piece_size} KB")

if __name__ == "__main__":
    
    main()