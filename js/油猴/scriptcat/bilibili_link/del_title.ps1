Write-Host "txt-删除视频标题"

# 获取脚本文件的完整路径
$scriptPath = $MyInvocation.MyCommand.Path

# 获取脚本文件所在的文件夹
$scriptFolder = Split-Path $scriptPath -Parent

# 带标题 链接的txt，拼接路径
$resultPath = Join-Path -Path $scriptFolder -ChildPath "File.txt"

# 纯视频 链接 txt
$videolink = Join-Path -Path $scriptFolder -ChildPath "video_link.txt"

write-host "文件路径: $resultPath"

#  end ~~~~~~~~~~~~~~~~~

# 删除 ## st ~~~~~~~~~~~

# 读取文本文件内容
$fileContent = Get-Content -Path $resultPath -Raw

# 使用正则表达式替换
$modifiedContent = $fileContent -replace '(?m)^#.*?$|^.*?#\n$', ''

# 删除空行
$modifiedContent = $modifiedContent -replace '\n+', ""

# 将修改后的内容写回文本文件
$modifiedContent | Out-File -FilePath $videolink  -Encoding utf8

write-host `删除视频标题-操作完成 ${videolink}`

Pause