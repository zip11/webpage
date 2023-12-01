from flask import Flask, request
import os

# sock5 代理 服务器 网址
proxyip = ""

proxyip = "--proxy  socks5://" + proxyip

app = Flask(__name__)

# 保存 单个视频网址 到 txt
@app.route('/')
def hello():
    
    # 获取 get 参数
    name = request.args.get('name')
    
    # 视频网址，写入到 txt
    writetxt("video_link.txt",name)

    # 返回 下载完成提升
    return f'down_end_down_string:, {name}!'

# 批量视频 下载
@app.route("/dl")
def ph_yt():

    # 启动 批量下载 程序 
    os.system(f'yt-dlp  -f "best[height<=720]" --batch-file "video_link.txt" {proxyip}')
    return "Batch_download_end_yt-dlp!!!"

# 单个 视频下载
@app.route("/sdl")
def dl_yt():

    # 单个 视频 下载

    # 获取 get 参数
    name = request.args.get('name')

    print("sdl:"+name)
    
    if(name.find("pornhub")!= -1):

        # 启动 单个 下载 程序
        os.system(f'yt-dlp  -f "best[height<=720]" {name} {proxyip}')
    
    elif(name.find("bilibili")!= -1):

        # bilibili 480p avc mp4
        os.system(f'yt-dlp  -f "bestvideo[height<=480]+bestaudio" {name} ')
    
    elif(name.find("youtube")!= -1):

        # youtube 480p mp4
        os.system(f'yt-dlp  -f "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]"  {name} {proxyip}')


    
    return f"download_end_yt-dlp: {name} !!!"

def writetxt(tfile,strtxt):

    # 添加 内容 到 txt
    with open(tfile, 'a') as f:

        # 读取 txt
        txtnr = readtxt(tfile)
        
        # txt 内容 为 空
        if(txtnr == ""):
            f.write(strtxt)
        else:

            # 有内容，不换行
            f.write('\n'+strtxt)
        


def readtxt(tfile):

    # 读取 txt

    import os

    # 判断 文件是否 存在
    if os.path.exists(tfile) == False:
        os.mknod(tfile)

    # 读取 一行 txt
    with open(tfile, 'r', encoding='utf-8') as f:

        data = f.readline()
        print(data)

        # 返回 第一行 文本
        return data


if __name__ == '__main__':
    app.run(debug=True)
