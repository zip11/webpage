Write-Host "����mp3��u��"

# ��ȡָ�� ��� �� ���� ��
$disk_name = ""
$disk_name = "m"
$Volume = Get-WmiObject -Class Win32_Volume -Filter "Label='$disk_name'"
Write-Host "u��·��: " $Volume.DriveLetter

# mp3 ·��
$folderpath = Read-Host -Prompt "MP3�����ļ���·��"

# ƴ�� u�� ȫ·��
$destpath = Join-Path -Path $Volume.DriveLetter -ChildPath "music"

# �����ļ��� 
# Copy-Item -Path $folderpath -Destination $destpath -Recurse

Get-ChildItem -Path $folderPath -File  | ForEach-Object {
     Copy-Item $_.FullName -Destination $destpath
     Write-Host "�����ļ�end: " $_.FullName
}


Write-Host "�������"
Pause