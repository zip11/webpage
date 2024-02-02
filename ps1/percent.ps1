# 进度条

$totalItems = 100
for ($i = 1; $i -le $totalItems; $i++) {
    Start-Sleep -Milliseconds 50 # 模拟耗时操作

    $percentComplete = ($i / $totalItems) * 100
    Write-Progress -Activity "正在进行处理" `
                   -Status "已完成 $($i) 项, 共 $($totalItems) 项" `
                   -PercentComplete $percentComplete
}

Write-Progress -Activity "正在进行处理" -Completed