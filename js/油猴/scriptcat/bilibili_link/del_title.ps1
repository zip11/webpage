Write-Host "txt-ɾ����Ƶ����"

# ��ȡ�ű��ļ�������·��
$scriptPath = $MyInvocation.MyCommand.Path

# ��ȡ�ű��ļ����ڵ��ļ���
$scriptFolder = Split-Path $scriptPath -Parent

# ������ ���ӵ�txt��ƴ��·��
$resultPath = Join-Path -Path $scriptFolder -ChildPath "File.txt"

# ����Ƶ ���� txt
$videolink = Join-Path -Path $scriptFolder -ChildPath "video_link.txt"

write-host "�ļ�·��: $resultPath"

#  end ~~~~~~~~~~~~~~~~~

# ɾ�� ## st ~~~~~~~~~~~

# ��ȡ�ı��ļ�����
$fileContent = Get-Content -Path $resultPath -Raw

# ʹ��������ʽ�滻
$modifiedContent = $fileContent -replace '(?m)^#.*?$|^.*?#\n$', ''

# ɾ������
$modifiedContent = $modifiedContent -replace '\n+', ""

# ���޸ĺ������д���ı��ļ�
$modifiedContent | Out-File -FilePath $videolink  -Encoding utf8

write-host `ɾ����Ƶ����-������� ${videolink}`

Pause