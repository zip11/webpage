Write-Host "����mp3��u��"

# ��ȡָ�� ��� �� ���� ��
$disk_name = ""

$Volume = Get-WmiObject -Class Win32_Volume -Filter "Label='$disk_name'"
$Volume.DriveLetter

# mp3 ·��
$folderpath = Read-Host -Prompt "�����ļ���·��"

# ƴ�� u�� ȫ·��
$destpath = Join-Path -Path $Volume.DriveLetter -ChildPath "music"

# �����ļ��� 
Copy-Item -Path $folderpath -Destination $destpath -Recurse

Write-Host "�������"
Pause