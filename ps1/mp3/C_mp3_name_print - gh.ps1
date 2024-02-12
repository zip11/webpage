# 打印mp3 文件名 到 txt

write-host "打印mp3 文件名 到 txt"

# 获取指定 存储卡 卷标， 的 分区 号
$disk_name = ""
$disk_name = "m"
$Volume = Get-WmiObject -Class Win32_Volume -Filter "Label='$disk_name'"
Write-Host "u盘路径: " $Volume.DriveLetter

# 拼接 u盘 全路径
$destpath = Join-Path -Path $Volume.DriveLetter -ChildPath "music"

# 获取ps1文件的目录
$dir = (Get-Item -Path $MyInvocation.MyCommand.Path).DirectoryName
write-host "Directory: $dir"


# 获取文件夹下 所有文件名
$files = Get-ChildItem -Path $destpath -File | ForEach-Object {$_.Name}

# 打印文件名,两个名字为一组

$files | ForEach-Object {Write-Host $_}

Write-Host "搜索mp3完成"

# 文件名 保存到 txt ~~~~~~
$txt_path = join-path -Path $dir -ChildPath "mp3_name_print.txt"

$files | Out-File -FilePath $txt_path -Encoding utf8


Write-Host "txt保存完成"

Pause