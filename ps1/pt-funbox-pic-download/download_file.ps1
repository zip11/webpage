Write-Host "批量下载文件，通过links.txt文件内的网址"

# 油猴下载文件，文件太大，下载只能部分，下载速度也慢

# power shell 下载文件，读取txt文件内容是每一行都是一个下载链接，
# 下载文件名为 数字序号，把下载文件存放入 今天 年月日 组成的数字 文件夹

# st ~~~~~~~
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
    write-host "文件夹 $folderPath 创建成功"
}

# end ~~~~~~~~~~


# 下载 链接 数量 st ~~~~~~~~~~~~~~~
$counter = 1

# 遍历 txt 下载链接
foreach ($link in $links) {

    # 输出2位数字，不足补0
    $fileName = "{0:d2}.jpg" -f $counter
    # 下载文件 全路径
    $filePath = Join-Path $folderPath $fileName

    # $links的数量
    $total = $links.Count
    # 显示 下载进度
    write-host "Downloading $fileName..., current/total_number:$counter/$total"

    # 下载文件，无进度条
    # Invoke-WebRequest -Uri $link -OutFile $filePath

    # 后台下载，进度条
    Start-BitsTransfer -Source $link -Destination $filePath
    $counter = $counter + 1
}

write-host "Download complete."

# end ~~~~~~~

# txt文件复制 新txt，文件名是年月日，清空txt

$newTxtPath = Join-Path -Path $folderPath -ChildPath "nc_pic_$date.txt"
Copy-Item -Path $txtPath -Destination $newTxtPath
Clear-Content -Path $txtPath

write-host "New txt file created: $newTxtPath end !!!"

Pause