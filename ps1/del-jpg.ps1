
# 输入文件夹路径
$folderPath = Read-Host "请输入文件夹路径"

# 替换为你的文件夹路径
# $folderPath = "C:\Path\To\Your\Folder"

# 获取所有子文件夹
$subfolders = Get-ChildItem -Path $folderPath -Directory

# 遍历每个子文件夹
foreach ($subfolder in $subfolders) {

    # 构建 JPG 文件的路径模式
    $jpgPattern = Join-Path -Path $subfolder.FullName -ChildPath "*.jpg"

    # 删除匹配的 JPG 文件
    Remove-Item -Path $jpgPattern -Force
    write-host "Deleted JPG files in $($subfolder.FullName)"
}

Write-Host "JPG files in subfolders deleted successfully."
