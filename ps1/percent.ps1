# ������

$totalItems = 100
for ($i = 1; $i -le $totalItems; $i++) {
    Start-Sleep -Milliseconds 50 # ģ���ʱ����

    $percentComplete = ($i / $totalItems) * 100
    Write-Progress -Activity "���ڽ��д���" `
                   -Status "����� $($i) ��, �� $($totalItems) ��" `
                   -PercentComplete $percentComplete
}

Write-Progress -Activity "���ڽ��д���" -Completed