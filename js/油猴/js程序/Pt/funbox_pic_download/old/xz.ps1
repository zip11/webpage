Write-Host "批量下载文件，通过txt文件链接"

# 油猴下载文件，文件太大，下载只能部分，下载速度也慢

# power shell 下载文件，读取txt文件内容是每一行都是一个下载链接，
# 下载文件名为 数字序号，把下载文件存放入 今天 年月日 组成的数字 文件夹

# 获取脚本文件的完整路径
$scriptPath = $MyInvocation.MyCommand.Path

# 获取脚本文件所在的文件夹
$scriptFolder = Split-Path $scriptPath -Parent

# txt文件 全路径
$txtPath = Join-Path -Path $scriptFolder -ChildPath "links.txt"
$links = Get-Content -Path $txtPath

# 下载文件夹 全路径 
$date = Get-Date -Format yyyyMMdd
$folderPath = Join-Path -Path $scriptFolder -ChildPath $date

# 判断 下载 文件夹 是否存在
if (!(Test-Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath | Out-Null
}


# 下载 链接 数量
$counter = 1

# 遍历 txt 下载链接
foreach ($link in $links) {

    # 下载文件 全路径
    $fileName = "$counter.jpg"
    $filePath = Join-Path $folderPath $fileName

    # $links的数量
    $total = $links.Count
    write-host "Downloading $fileName..., current/total_number:$counter/$total"

    # 下载文件
    Invoke-WebRequest -Uri $link -OutFile $filePath
    $counter++
}

write-host "Download complete."

Pause