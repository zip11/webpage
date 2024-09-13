Write-Host "批量下载文件，通过links.txt文件内的网址"

# 从 JSON 文件中读取代理信息
$jsonFile = Join-Path $PSScriptRoot -ChildPath "proxy.json"

if (!(Test-Path $jsonFile)) {
    Write-Host "代理信息文件 $jsonFile 不存在，请检查文件路径。"
    return
}

$proxyInfo = Get-Content -Raw -Path $jsonFile | ConvertFrom-Json
$proxy = "http://$($proxyInfo.proxy):$($proxyInfo.port)"
# $proxyCredential = Get-Credential

# 显示代理信息
Write-Host "Proxy: $proxy"

# pause code
Pause


# st ~~~~~~~
# 获取脚本文件的完整路径
$scriptPath = $MyInvocation.MyCommand.Path

# 获取脚本文件所在的文件夹
$scriptFolder = Split-Path $scriptPath -Parent

# txt文件 全路径
$txtPath = Join-Path -Path $scriptFolder -ChildPath "links.txt"
$links = Get-Content -Path $txtPath

# txt检查是否存在
if (!(Test-Path $txtPath)) {
    Write-Host "文件 $txtPath 不存在，请检查文件路径。"
    pause
    return
}

# end ~~~~~~~~~~

# 下载文件夹 全路径 
$date = Get-Date -Format yyyyMMdd
$folderPath = Join-Path -Path $scriptFolder -ChildPath $date

# 判断 下载 文件夹 是否存在
if (!(Test-Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath | Out-Null
    Write-Host "文件夹 $folderPath 创建成功"
}

# end ~~~~~~~~~~

# 下载 链接 数量 st ~~~~~~~~~~~~~~~
$counter = 1

# 遍历 txt 下载链接
foreach ($link in $links) {

    # 输出3位数字，不足补0
    $fileName = "{0:d3}.jpg" -f $counter
    # 下载文件 全路径
    $filePath = Join-Path $folderPath $fileName

    # $links的数量
    $total = $links.Count
    # 创建进度记录
    $progressParams = @{
        Activity = "Downloading $fileName"
        Status = "Downloading file $counter of $total"
        PercentComplete = ($counter / $total) * 100
    }
    Write-Progress @progressParams



    # 代理下载
    Invoke-WebRequest -Uri $link -OutFile $filePath -Proxy $proxy 

    
    # 代理服务器  用户名，密码
    # -ProxyCredential $proxyCredential

    $counter = $counter + 1
}

Write-Progress -Activity "Download Complete" -Completed

Write-Host "Download complete."

# end ~~~~~~~

# 新txt文件名，文件名是年月日，清空txt
$newTxtPath = Join-Path -Path $folderPath -ChildPath "nc_pic_$date.txt"

# $txtPath 复制文件 到 $newTxtPath
Copy-Item -Path $txtPath -Destination $newTxtPath
# 删除 $txtPath
Remove-Item -Path $txtPath

Write-Host "New txt file created: $newTxtPath end !!!"

Pause
