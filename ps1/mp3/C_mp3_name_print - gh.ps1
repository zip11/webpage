# ��ӡmp3 �ļ��� �� txt

write-host "��ӡmp3 �ļ��� �� txt"

# ��ȡָ�� �洢�� ��꣬ �� ���� ��
$disk_name = ""
$disk_name = "m"
$Volume = Get-WmiObject -Class Win32_Volume -Filter "Label='$disk_name'"
Write-Host "u��·��: " $Volume.DriveLetter

# ƴ�� u�� ȫ·��
$destpath = Join-Path -Path $Volume.DriveLetter -ChildPath "music"

# ��ȡps1�ļ���Ŀ¼
$dir = (Get-Item -Path $MyInvocation.MyCommand.Path).DirectoryName
write-host "Directory: $dir"


# ��ȡ�ļ����� �����ļ���
$files = Get-ChildItem -Path $destpath -File | ForEach-Object {$_.Name}

# ��ӡ�ļ���,��������Ϊһ��

$files | ForEach-Object {Write-Host $_}

Write-Host "����mp3���"

# �ļ��� ���浽 txt ~~~~~~
$txt_path = join-path -Path $dir -ChildPath "mp3_name_print.txt"

$files | Out-File -FilePath $txt_path -Encoding utf8


Write-Host "txt�������"

Pause