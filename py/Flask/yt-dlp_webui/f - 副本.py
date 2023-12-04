from flask import Flask, request
import os

# sock5 代理 服务器 网址
proxyip = ""

proxyip = "--proxy  socks5://" + proxyip

# ph save path
phpath_folder = "YT"
phpath = f""" -o ".\{phpath_folder}\%(title)s.%(ext)s" """

# batch file
batchfile = ""


app = Flask(__name__)

# 保存 单个视频网址 到 txt ~~~~~~start~~~~~~~
@app.route('/')
def savetxt():
    
    # 获取 get 参数
    name = request.args.get('name')
    
    # 视频网址，写入到 txt
    writetxt(batchfile,name)

    # 返回 下载完成提升
    return f'down_end_down_string:, {name}!'

# 批量视频 下载 ~~~~~~start~~~~~~~
@app.route("/dl")
def pl_xz():

    # 启动 批量下载 程序 
    save_video_pl()

    return "Batch_download_end_yt-dlp!!!"


# 清空 批量视频 txt  ~~~~~~start~~~~~~~
@app.route("/del")
def pl_del():

    # del txt 批量下载 
    with open(batchfile, 'w') as f:

        f.write('')
    
    return "clear_Batch_download_txt ok!!!"


# 单个 视频下载 ~~~~~~start~~~~~~~
@app.route("/sdl")
def dl_yt():

    # 单个 视频 下载
    # 获取 get 参数
    name2 = request.args.get('name')

    print("sdl:"+name2)

    save_video(name2)

    
    return f"download_end_yt-dlp: {name2} !!!"



# 下载 单个 视频 ~~~~~~start~~~~~~~
def save_video(name):

    
    # 判断 网址
    if(name.find("pornhub")!= -1):

        phpath_folder = "Ph"
        phpath = f""" -o ".\{phpath_folder}\%(title)s.%(ext)s" """
        # 启动 单个 下载 程序
        os.system(f'yt-dlp  -f "best[height<=720]" {name} {phpath} {proxyip}')
    
    elif(name.find("bilibili")!= -1):

        phpath_folder = "bilibili"
        phpath = f""" -o ".\{phpath_folder}\%(title)s.%(ext)s" """
        # bilibili 480p avc mp4
        os.system(f'yt-dlp  -f "bestvideo[height<=480]+bestaudio" {name} {phpath}')
    
    elif(name.find("youtube")!= -1):

        phpath_folder = "Yt"
        phpath = f""" -o ".\{phpath_folder}\%(title)s.%(ext)s" """
        # youtube 480p mp4
        os.system(f'yt-dlp  -f "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]"  {name} {phpath} {proxyip}')


# 批量下载 视频 ~~~~~~start~~~~~~~
def save_video_pl():

    

    # 读取 txt,第一行
    name = readtxt(batchfile)

    
    # batch command
    batch_command = f' --batch-file {batchfile} '

    # 判断 网站
    if(name.find("pornhub")!= -1):

        phpath_folder = "Ph"
        phpath = f""" -o ".\{phpath_folder}\%(title)s.%(ext)s" """
        # 启动 单个 下载 程序
        os.system(f'yt-dlp  -f "best[height<=720]" {batch_command} {phpath} {proxyip}')
    
    elif(name.find("bilibili")!= -1):

        phpath_folder = "bilibili"
        phpath = f""" -o ".\{phpath_folder}\%(title)s.%(ext)s" """
        # bilibili 480p avc mp4
        os.system(f'yt-dlp  -f "bestvideo[height<=480]+bestaudio" {batch_command} {phpath}')
    
    elif(name.find("youtube")!= -1):

        phpath_folder = "Yt"
        phpath = f""" -o ".\{phpath_folder}\%(title)s.%(ext)s" """
        # youtube 480p mp4
        os.system(f'yt-dlp  -f "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]"  {batch_command} {phpath} {proxyip}')

# 生成 日期  txt 名字 ~~~~~~start~~~~~~~
def txtname():

    import time
    txtfile = time.strftime("%Y%m%d ", time.localtime()) 
    txtfile = "video_link_" + txtfile + ".txt" 

    return txtfile

# 保存网址 到txt ~~~~~~start~~~~~~~
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
        

# 读取txt ~~~~~~start~~~~~~~
def readtxt(tfile):

    # 读取 txt,第一行内容

    import os

    # 判断 文件是否 存在
    if os.path.exists(tfile) == False:
        # 新建 空文件
        os.mknod(tfile)
        # 返回 ""
        return ""

    # 读取 一行 txt
    with open(tfile, 'r', encoding='utf-8') as f:

        data = f.readline()
        print(data)

        # 返回 第一行 文本
        return data


if __name__ == '__main__':

    # 日期 txt
    batchfile = txtname()
    app.run(debug=True)
