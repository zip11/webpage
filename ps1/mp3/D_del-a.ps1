# ��ȡps1�ļ���Ŀ¼
# $dir = (Get-Item -Path $MyInvocation.MyCommand.Path).DirectoryName
# write-host "Directory: $dir"

write-host "ɾ�����������еģ� A����λ����_"

$music_path = Read-Host "��������ļ���·��"

# ��ǰĿ¼ �£��ļ����� ��ͷ��A����λ���֣�ɾ��A����λ����
Get-ChildItem -Path $music_path -Filter "A*" | ForEach-Object {
    
    $fileName = $_.Name
    # ��ȡ�ļ���
  
    # ɾ��4λ����
    $newFileName = $fileName -replace "A\d{4}_", ""

    # �������ļ�
    Rename-Item -Path $_.FullName -NewName $newFileName
    write-host "Renamed file: $newFileName"
}
