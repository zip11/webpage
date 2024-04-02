write-host "��ȡjson�ļ�����Ƶ��ַ��ʹ��yt-dlp������Ƶ������"


# yt_dlp ������ļ���·��
$ytdlp = "D:\app\net\yt-dlp"
# ���� ȫ·��
$ytdlp = Join-Path -Path $ytdlp -ChildPath "yt-dlp.exe"

# ��������Ŀ¼
$downloadDirectory = "$PSScriptRoot\Ph"


#��ȡjson�ļ�����Ĵ���ip�Ͷ˿�
$proxy = Get-Content "$PSScriptRoot\proxy.json" | ConvertFrom-Json
$proxy_address = $proxy.proxy_address
$proxy_port = $proxy.proxy_port

# ��ȡ JSON �ļ��е���ַ
$json_folder = "$PSScriptRoot"

# ��ȡ��ǰ���ڲ���ʽ��Ϊ YYYY_MM_DD ��ʽ
$today = Get-Date -Format "yyyy_MM_dd"

# ���� JSON �ļ��������� bookmarks_YYYY_MM_DD.json
$jsonFileName = "bookmarks_$today.json"

# ��� JSON �ļ���
Write-Host "JSON �ļ���: $jsonFileName"

$json_file = $jsonFileName

$jsonFile_all = Join-Path -Path $json_folder -ChildPath $json_file

$jsonContent = Get-Content "$jsonFile_all" | ConvertFrom-Json

# ��ǰ��������
$i = 0
# ȫ������ ����
$total = $jsonContent.Count

# ����ÿ����ַ��������Ƶ
foreach ($item in $jsonContent) {

    # json��url ��ַ
    $url = $item.url
    Write-Host "Downloading $url..."

    & ${ytdlp} --output "$downloadDirectory\%(title)s.%(ext)s" --format "best[height<=720]" --proxy socks5://${proxy_address}:$proxy_port $url
    
    $i = $i + 1
    Write-Host "Downloaded $i of $total"

}
Write-Host "All downloads completed."

# $jsonFile �����ļ� Ϊ�ļ���  ������_$jsonFile

# ���� ������ �ַ���
$dateString = Get-Date -Format "yyyyMMdd"
# ��ȡ �ļ���������չ��
$fileNameWithoutExtension = [System.IO.Path]::GetFileNameWithoutExtension($json_File)

# ���ļ���
$newFileName = $dateString + "_" + $fileNameWithoutExtension + ".json"

# ���ļ��� ȫ·��
$newFileName = Join-Path -Path $json_folder  -ChildPath $newFileName

Copy-Item $jsonFile_all -Destination $newFileName

write-host "�ѱ������ؼ�¼ $newFileName"

Pause