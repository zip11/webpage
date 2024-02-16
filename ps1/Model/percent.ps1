# ������
function Show-ProgressExample {
    param (
        [int]$TotalItems,
        [string]$Activity = "Processing Items"
    )

    for ($i = 1; $i -le $TotalItems; $i++) {
        # ��������ɰٷֱ�
        $percentComplete = ($i / $TotalItems) * 100

        # ��ʾ������
        Write-Progress -Activity $Activity -Status "Processing item $i of $TotalItems" -PercentComplete $percentComplete

        # ģ�⴦��ÿ����Ŀ�����ʱ�䣨���磺����һ�룩
        Start-Sleep -Milliseconds 500
    }

    # ��������Ŀ��ɺ󣬹رս�����
    Write-Progress -Activity $Activity -Completed
}

# ʹ�ú���
Show-ProgressExample -TotalItems 20
