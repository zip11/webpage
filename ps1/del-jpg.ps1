
# �����ļ���·��
$folderPath = Read-Host "�������ļ���·��"

# �滻Ϊ����ļ���·��
# $folderPath = "C:\Path\To\Your\Folder"

# ��ȡ�������ļ���
$subfolders = Get-ChildItem -Path $folderPath -Directory

# ����ÿ�����ļ���
foreach ($subfolder in $subfolders) {

    # ���� JPG �ļ���·��ģʽ
    $jpgPattern = Join-Path -Path $subfolder.FullName -ChildPath "*.jpg"

    # ɾ��ƥ��� JPG �ļ�
    Remove-Item -Path $jpgPattern -Force
    write-host "Deleted JPG files in $($subfolder.FullName)"
}

Write-Host "JPG files in subfolders deleted successfully."
