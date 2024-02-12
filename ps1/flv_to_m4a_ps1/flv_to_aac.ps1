# flv转m4a,无损复制音频 aac

function flvtom4a {
    param (
        [string]$file_path
    )

    # $PSScriptRoot 获取所有flv文件，使用ffmpeg ，把flv视频转换到纯音频的m4a格式
    $files = Get-ChildItem -Path $file_path -Filter *.flv

    foreach ($file in $files)
    {

        # 输出转换后的文件名
        $outputFilePath = Join-Path -Path $file_path -ChildPath "$($file.BaseName).m4a"

        # 使用ffmpeg进行转换
        ffmpeg -i $file.FullName -vn -c:a copy  $outputFilePath

        Write-Output "转换完成: $outputFilePath"

        # 删除 flv
        Remove-Item -Path $file.FullName
    }
    
}

# 定义读取JSON文件并获取文件路径列表的函数
function Get-FilePathsFromJson {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory=$true)]
        [string]$JsonFilePath
    )

    # 读取JSON内容并转换为 PowerShell 对象
    $jsonContent = Get-Content -Path $JsonFilePath -Raw | ConvertFrom-Json

    # 假设JSON对象内有一个名为"filePaths"的数组属性，其中包含了所有文件路径
    if ($jsonContent.filePaths) {
        return $jsonContent.filePaths
    } else {
        Write-Error "JSON文件中未找到'filePaths'属性或其值为空。"
        return $null
    }
}


# 获取 ps1文件的目录 路径
# Write-Host "ps1-file-path: $PSScriptRoot"


# 拼接 json文件路径
$jsonFilePath = Join-Path -Path $PSScriptRoot -ChildPath "file_paths.json"
write-host "json-file-path: $jsonFilePath"

# 获取json，路径
$filePaths = Get-FilePathsFromJson -JsonFilePath $jsonFilePath

# 现在可以遍历文件路径数组进行操作
foreach ($filePath in $filePaths) {

    Write-Host "处理文件: $filePath"
    # 视频 转 音频
    flvtom4a -file_path $filePath
}

write-host "转换完成"



# ffmpeg
# -i input.flv 指定输入文件是名为“input.flv”的FLV格式视频文件。
# -vn 表示不包含视频流（Video No），即输出时不包含视频内容。
# -c:a copy 设置音频流直接复制（Copy）到输出文件，这意味着音频不会经过重新编码，从而保持原音质不变。
# output.m4a 是输出文件名，最终生成的音频文件将以M4A格式存储，并且其音频部分与源FLV文件完全相同。





#

