# 获取网址末尾的exe程序 名字
$url = "https://cdn.aliyundrive.net/downloads/apps/desktop/aDrive-4.12.0.exe"

write-host "进度条-后台-下载文件: $url"

# 获取url的最后一个元素，作为文件名
$filename = $url.Split('/')[-1]

# 下载文件到指定目录
$destination = "d:\"
Start-BitsTransfer -Source $url -Destination $destination$filename

