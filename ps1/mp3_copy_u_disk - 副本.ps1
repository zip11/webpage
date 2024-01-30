Write-Host "复制mp3到u盘"

# 获取指定 卷标 的 分区 号
$disk_name = ""

$Volume = Get-WmiObject -Class Win32_Volume -Filter "Label='$disk_name'"
$Volume.DriveLetter

# mp3 路径
$folderpath = Read-Host -Prompt "输入文件夹路径"

# 拼接 u盘 全路径
$destpath = Join-Path -Path $Volume.DriveLetter -ChildPath "music"

# 复制文件夹 
Copy-Item -Path $folderpath -Destination $destpath -Recurse

Write-Host "复制完成"
Pause