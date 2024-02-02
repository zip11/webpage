# $PSDefaultParameterValues['*:Encoding'] = 'utf8'


# 提示用户输入文件夹路径
$folderPath = Read-Host "请输入包含JPG文件的文件夹路径"

# pic 
$pic_ext = "webp"

# 创建 jxl 新文件夹
$jxlfolder = $folderPath + "_" + $pic_ext
New-Item -ItemType Directory -Force -Path $jxlFolder | Out-Null
write-host "已创建 _jxl 文件夹,$jxlFolder"

# 遍历指定文件夹下所有jpg文件
Get-ChildItem -Path $folderPath -Filter *.jpg -Recurse | ForEach-Object {

    # 获取当前jpg文件的完整路径
    $jpegFile = $_.FullName

    # 计算输出文件名（保持在相同目录，只改变扩展名为.jxl）
    # $jxlFile = $jxlFolder + "\" + $_.BaseName + ".jxl"

    # 计算输出文件名（保持在相同目录，只改变扩展名为.jxl）
    $jxlFile = $jxlfolder + "\" + $_.BaseName + "." + $pic_ext

    # 使用cjxl命令进行无损转换
    # & "D:\Program Files\libjxl\cjxl.exe" $jpegFile $jxlFile

    # webp q=75
    ffmpeg -i "$jpegFile" -vf scale=-2:4320 -c:v libwebp -q:v 75  "$jxlFile"
    
    write-host "转换 $jpegFile => $jxlFile"
}

Write-Host "转换完成！"

Pause