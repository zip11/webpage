write-host "获取json文件内视频网址，使用yt-dlp下载视频！！！"


# yt_dlp 程序的文件夹路径
$ytdlp = "D:\app\net\yt-dlp"
# 程序 全路径
$ytdlp = Join-Path -Path $ytdlp -ChildPath "yt-dlp.exe"

# 设置下载目录
$downloadDirectory = "$PSScriptRoot\Ph"


#读取json文件保存的代理ip和端口
$proxy = Get-Content "$PSScriptRoot\proxy.json" | ConvertFrom-Json
$proxy_address = $proxy.proxy_address
$proxy_port = $proxy.proxy_port

# 读取 JSON 文件中的网址
$json_folder = "$PSScriptRoot"
$json_file = "bookmarks.json"

$jsonFile_all = Join-Path -Path $json_folder -ChildPath $json_file

$jsonContent = Get-Content "$jsonFile_all" | ConvertFrom-Json

# 当前下载数量
$i = 0
# 全部下载 数量
$total = $jsonContent.Count

# 遍历每个网址并下载视频
foreach ($item in $jsonContent) {

    # json的url 网址
    $url = $item.url
    Write-Host "Downloading $url..."

    & ${ytdlp} --output "$downloadDirectory\%(title)s.%(ext)s" --format "best[height<=720]" --proxy socks5://${proxy_address}:$proxy_port $url
    
    $i = $i + 1
    Write-Host "Downloaded $i of $total"

}
Write-Host "All downloads completed."

# $jsonFile 复制文件 为文件名  年月日_$jsonFile

# 生成 年月日 字符串
$dateString = Get-Date -Format "yyyyMMdd"
# 获取 文件名，无扩展名
$fileNameWithoutExtension = [System.IO.Path]::GetFileNameWithoutExtension($json_File)

# 新文件名
$newFileName = $dateString + "_" + $fileNameWithoutExtension + ".json"

# 新文件名 全路径
$newFileName = Join-Path -Path $json_folder  -ChildPath $newFileName

Copy-Item $jsonFile_all -Destination $newFileName

write-host "已保存下载记录 $newFileName"

Pause