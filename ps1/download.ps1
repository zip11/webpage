# ��ȡ��ַĩβ��exe���� ����
$url = "https://cdn.aliyundrive.net/downloads/apps/desktop/aDrive-4.12.0.exe"

write-host "������-��̨-�����ļ�: $url"

# ��ȡurl�����һ��Ԫ�أ���Ϊ�ļ���
$filename = $url.Split('/')[-1]

# �����ļ���ָ��Ŀ¼
$destination = "d:\"
Start-BitsTransfer -Source $url -Destination $destination$filename

