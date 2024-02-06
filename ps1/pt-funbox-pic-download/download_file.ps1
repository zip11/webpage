Write-Host "���������ļ���ͨ��links.txt�ļ��ڵ���ַ"

# �ͺ������ļ����ļ�̫������ֻ�ܲ��֣������ٶ�Ҳ��

# power shell �����ļ�����ȡtxt�ļ�������ÿһ�ж���һ���������ӣ�
# �����ļ���Ϊ ������ţ��������ļ������ ���� ������ ��ɵ����� �ļ���

# st ~~~~~~~
# ��ȡ�ű��ļ�������·��
$scriptPath = $MyInvocation.MyCommand.Path

# ��ȡ�ű��ļ����ڵ��ļ���
$scriptFolder = Split-Path $scriptPath -Parent

# txt�ļ� ȫ·��
$txtPath = Join-Path -Path $scriptFolder -ChildPath "links.txt"
$links = Get-Content -Path $txtPath

# �����ļ��� ȫ·�� 
$date = Get-Date -Format yyyyMMdd
$folderPath = Join-Path -Path $scriptFolder -ChildPath $date

# �ж� ���� �ļ��� �Ƿ����
if (!(Test-Path $folderPath)) {
    New-Item -ItemType Directory -Path $folderPath | Out-Null
    write-host "�ļ��� $folderPath �����ɹ�"
}

# end ~~~~~~~~~~


# ���� ���� ���� st ~~~~~~~~~~~~~~~
$counter = 1

# ���� txt ��������
foreach ($link in $links) {

    # ���2λ���֣����㲹0
    $fileName = "{0:d2}.jpg" -f $counter
    # �����ļ� ȫ·��
    $filePath = Join-Path $folderPath $fileName

    # $links������
    $total = $links.Count
    # ��ʾ ���ؽ���
    write-host "Downloading $fileName..., current/total_number:$counter/$total"

    # �����ļ����޽�����
    # Invoke-WebRequest -Uri $link -OutFile $filePath

    # ��̨���أ�������
    Start-BitsTransfer -Source $link -Destination $filePath
    $counter = $counter + 1
}

write-host "Download complete."

# end ~~~~~~~

# txt�ļ����� ��txt���ļ����������գ����txt

$newTxtPath = Join-Path -Path $folderPath -ChildPath "nc_pic_$date.txt"
Copy-Item -Path $txtPath -Destination $newTxtPath
Clear-Content -Path $txtPath

write-host "New txt file created: $newTxtPath end !!!"

Pause