# 进度条
function Show-ProgressExample {
    param (
        [int]$TotalItems,
        [string]$Activity = "Processing Items"
    )

    for ($i = 1; $i -le $TotalItems; $i++) {
        # 计算已完成百分比
        $percentComplete = ($i / $TotalItems) * 100

        # 显示进度条
        Write-Progress -Activity $Activity -Status "Processing item $i of $TotalItems" -PercentComplete $percentComplete

        # 模拟处理每个项目所需的时间（例如：休眠一秒）
        Start-Sleep -Milliseconds 500
    }

    # 当所有项目完成后，关闭进度条
    Write-Progress -Activity $Activity -Completed
}

# 使用函数
Show-ProgressExample -TotalItems 20
