# 获取脚本文件的完整路径
$scriptPath = $MyInvocation.MyCommand.Path

# 获取脚本文件所在的文件夹
$scriptFolder = Split-Path $scriptPath -Parent


# 设置输入文件夹路径和输出文件夹路径
$inputFolder = $scriptFolder  # 替换为你的输入文件夹路径
$outputFolder = $scriptFolder  # 替换为你的输出文件夹路径

# 确保输出文件夹存在，如果不存在则创建
if (-not (Test-Path -Path $outputFolder)) {
    New-Item -ItemType Directory -Path $outputFolder | Out-Null
}

# 获取输入文件夹中的所有 MP4 文件
$mp4Files = Get-ChildItem -Path $inputFolder -Filter *.mp4

# 遍历每个 MP4 文件并进行无损转换到 AAC 音频
foreach ($mp4File in $mp4Files) {

    $outputFile = Join-Path $outputFolder ($mp4File.BaseName + ".aac")
    & ffmpeg -i $mp4File.FullName -c:a aac  -map_metadata 0 -id3v2_version 3 $outputFile
    Write-Host "已将 $($mp4File.Name) 转换为 $($mp4File.BaseName).aac"
}

Write-Host "转换完成"
Pause