Write-Host "mp3 �ļ�������ӣ� 4λ �������"

# input st ~~~~~~~~~~~~~~

# ָ���ļ���·��
$folderPath = Read-Host "�������ļ���·��"

$num = Read-Host "�����ļ���-��ʼ����-��ţ�����������Ĭ��Ϊ1"

if ($num.Length -eq 0) {

    Write-Host "�ַ���Ϊ��"
    $num = 0
} else {
    
    Write-Host "�ַ�����Ϊ��"
    try {
        $num = [int]$num - 1
        # Write-Host "�ַ���ת��Ϊ�����ɹ�"

    } catch {
        Write-Host "�޷����ַ���ת��Ϊ����"
    }
}

# end ~~~~~~~~~




# ��ȡ�ļ����µ��ļ��б�
$fileList = Get-ChildItem -Path $folderPath | Where-Object { $_.PSIsContainer -eq $false }

<# 
Where-Object ������ڹ��˽����ֻ�������ļ��е��ļ���

$_.PSIsContainer ���ԣ������ж�һ�������Ƿ�Ϊ�ļ��С�����������ļ��У��򷵻� $true�����򷵻� $false��
  $false�����ڹ��˵��ļ��У�ֻ�����ļ���
#>

# ѭ�������ļ��б�Ϊ�ļ��������λ�������
foreach ($index in 0..($fileList.Count - 1)) {

    # ��� ���� ���� 0
    if ($num -ne 0) {
        $num = $num + 1
    } else {
        $num = $index + 1
    }

    # ƴ���µ��ļ���
    # ����һ������$newFileName�����ڴ洢����������ļ���
    $newFileName = "A{0:D4}_{1}" -f ($num), $fileList[$index].Name
    # ʹ��{0:D4}��ʽ���ַ��������ļ���ת��Ϊ4λ����
    
    # ʹ��-f��ʽ���ַ��������ļ���������ƴ��
    # $index �ַ��� ��ʼ��� 

    # ʹ��$fileList[$index].Name��ȡ�ļ���

    # ���ļ��� ��ƴ�� ȫ·��
    $newFilePath = Join-Path $folderPath $newFileName

    # ��ʾ ������
    write-host "�������ļ���$newFilePath`n"
    
    # �������ļ�
    Rename-Item -Path $fileList[$index].FullName -NewName $newFilePath
}

Write-Host "�ļ������������!"

Pause