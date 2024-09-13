Write-Host "���������ļ���ͨ��links.txt�ļ��ڵ���ַ"

# �� JSON �ļ��ж�ȡ������Ϣ
$jsonFile = Join-Path $PSScriptRoot -ChildPath "proxy.json"

if (!(Test-Path $jsonFile)) {
    Write-Host "������Ϣ�ļ� $jsonFile �����ڣ������ļ�·����"
    return
}

$proxyInfo = Get-Content -Raw -Path $jsonFile | ConvertFrom-Json
$proxy = "http://$($proxyInfo.proxy):$($proxyInfo.port)"
# $proxyCredential = Get-Credential

# ��ʾ������Ϣ
Write-Host "Proxy: $proxy"

# pause code
Pause


# st ~~~~~~~
# ��ȡ�ű��ļ�������·��
$scriptPath = $MyInvocation.MyCommand.Path

# ��ȡ�ű��ļ����ڵ��ļ���
$scriptFolder = Split-Path $scriptPath -Parent

# txt�ļ� ȫ·��
$txtPath = Join-Path -Path $scriptFolder -ChildPath "links.txt"
$links = Get-Content -Path $txtPath

# txt����Ƿ����
if (!(Test-Path $txtPath)) {
    Write-Host "�ļ� $txtPath �����ڣ������ļ�·����"
    pause
    return
}

# end ~~~~~~~~~~

# �����ļ��� ȫ·�� 
$date = Get-Date -Format yyyyMMdd
$folderPath = Join-Path -Path $scriptFolder -ChildPath $date

# �ж� ���� �ļ��� �Ƿ����
if (!(Test-Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath | Out-Null
    Write-Host "�ļ��� $folderPath �����ɹ�"
}

# end ~~~~~~~~~~

# ���� ���� ���� st ~~~~~~~~~~~~~~~
$counter = 1

# ���� txt ��������
foreach ($link in $links) {

    # ���3λ���֣����㲹0
    $fileName = "{0:d3}.jpg" -f $counter
    # �����ļ� ȫ·��
    $filePath = Join-Path $folderPath $fileName

    # $links������
    $total = $links.Count
    # �������ȼ�¼
    $progressParams = @{
        Activity = "Downloading $fileName"
        Status = "Downloading file $counter of $total"
        PercentComplete = ($counter / $total) * 100
    }
    Write-Progress @progressParams



    # ��������
    Invoke-WebRequest -Uri $link -OutFile $filePath -Proxy $proxy 

    
    # ���������  �û���������
    # -ProxyCredential $proxyCredential

    $counter = $counter + 1
}

Write-Progress -Activity "Download Complete" -Completed

Write-Host "Download complete."

# end ~~~~~~~

# ��txt�ļ������ļ����������գ����txt
$newTxtPath = Join-Path -Path $folderPath -ChildPath "nc_pic_$date.txt"

# $txtPath �����ļ� �� $newTxtPath
Copy-Item -Path $txtPath -Destination $newTxtPath
# ɾ�� $txtPath
Remove-Item -Path $txtPath

Write-Host "New txt file created: $newTxtPath end !!!"

Pause
