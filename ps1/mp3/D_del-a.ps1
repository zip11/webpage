# 获取ps1文件的目录
# $dir = (Get-Item -Path $MyInvocation.MyCommand.Path).DirectoryName
# write-host "Directory: $dir"

write-host "删除歌曲名字中的： A加四位数字_"

$music_path = Read-Host "输入歌曲文件夹路径"

# 当前目录 下，文件名是 开头是A加四位数字，删除A加四位数字
Get-ChildItem -Path $music_path -Filter "A*" | ForEach-Object {
    
    $fileName = $_.Name
    # 获取文件名
  
    # 删除4位数字
    $newFileName = $fileName -replace "A\d{4}_", ""

    # 重命名文件
    Rename-Item -Path $_.FullName -NewName $newFileName
    write-host "Renamed file: $newFileName"
}
