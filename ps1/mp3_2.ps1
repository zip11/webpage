Write-Host "mp3 文件批量添加， 4位 数字序号"

# input st ~~~~~~~~~~~~~~

# 指定文件夹路径
$folderPath = Read-Host "请输入文件夹路径"

$num = Read-Host "输入文件名-开始数字-序号，不输入数字默认为1"

if ($num.Length -eq 0) {

    Write-Host "字符串为空"
    $num = 0
} else {
    
    Write-Host "字符串不为空"
    try {
        $num = [int]$num - 1
        # Write-Host "字符串转换为整数成功"

    } catch {
        Write-Host "无法将字符串转换为整数"
    }
}

# end ~~~~~~~~~




# 获取文件夹下的文件列表
$fileList = Get-ChildItem -Path $folderPath | Where-Object { $_.PSIsContainer -eq $false }

<# 
Where-Object 命令：用于过滤结果，只保留非文件夹的文件。

$_.PSIsContainer 属性：用于判断一个对象是否为文件夹。如果对象是文件夹，则返回 $true，否则返回 $false。
  $false：用于过滤掉文件夹，只保留文件。
#>

# 循环遍历文件列表并为文件名添加四位数字序号
foreach ($index in 0..($fileList.Count - 1)) {

    # 如果 输入 不是 0
    if ($num -ne 0) {
        $num = $num + 1
    } else {
        $num = $index + 1
    }

    # 拼接新的文件名
    # 定义一个变量$newFileName，用于存储重命名后的文件名
    $newFileName = "A{0:D4}_{1}" -f ($num), $fileList[$index].Name
    # 使用{0:D4}格式化字符串，将文件名转换为4位数字
    
    # 使用-f格式化字符串，将文件名和数字拼接
    # $index 字符串 开始序号 

    # 使用$fileList[$index].Name获取文件名

    # 新文件名 ，拼接 全路径
    $newFilePath = Join-Path $folderPath $newFileName

    # 显示 重命名
    write-host "重命名文件：$newFilePath`n"
    
    # 重命名文件
    Rename-Item -Path $fileList[$index].FullName -NewName $newFilePath
}

Write-Host "文件名添加序号完成!"

Pause