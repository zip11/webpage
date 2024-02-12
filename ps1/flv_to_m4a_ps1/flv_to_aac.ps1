# flvתm4a,��������Ƶ aac

function flvtom4a {
    param (
        [string]$file_path
    )

    # $PSScriptRoot ��ȡ����flv�ļ���ʹ��ffmpeg ����flv��Ƶת��������Ƶ��m4a��ʽ
    $files = Get-ChildItem -Path $file_path -Filter *.flv

    foreach ($file in $files)
    {

        # ���ת������ļ���
        $outputFilePath = Join-Path -Path $file_path -ChildPath "$($file.BaseName).m4a"

        # ʹ��ffmpeg����ת��
        ffmpeg -i $file.FullName -vn -c:a copy  $outputFilePath

        Write-Output "ת�����: $outputFilePath"

        # ɾ�� flv
        Remove-Item -Path $file.FullName
    }
    
}

# �����ȡJSON�ļ�����ȡ�ļ�·���б�ĺ���
function Get-FilePathsFromJson {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory=$true)]
        [string]$JsonFilePath
    )

    # ��ȡJSON���ݲ�ת��Ϊ PowerShell ����
    $jsonContent = Get-Content -Path $JsonFilePath -Raw | ConvertFrom-Json

    # ����JSON��������һ����Ϊ"filePaths"���������ԣ����а����������ļ�·��
    if ($jsonContent.filePaths) {
        return $jsonContent.filePaths
    } else {
        Write-Error "JSON�ļ���δ�ҵ�'filePaths'���Ի���ֵΪ�ա�"
        return $null
    }
}


# ��ȡ ps1�ļ���Ŀ¼ ·��
# Write-Host "ps1-file-path: $PSScriptRoot"


# ƴ�� json�ļ�·��
$jsonFilePath = Join-Path -Path $PSScriptRoot -ChildPath "file_paths.json"
write-host "json-file-path: $jsonFilePath"

# ��ȡjson��·��
$filePaths = Get-FilePathsFromJson -JsonFilePath $jsonFilePath

# ���ڿ��Ա����ļ�·��������в���
foreach ($filePath in $filePaths) {

    Write-Host "�����ļ�: $filePath"
    # ��Ƶ ת ��Ƶ
    flvtom4a -file_path $filePath
}

write-host "ת�����"



# ffmpeg
# -i input.flv ָ�������ļ�����Ϊ��input.flv����FLV��ʽ��Ƶ�ļ���
# -vn ��ʾ��������Ƶ����Video No���������ʱ��������Ƶ���ݡ�
# -c:a copy ������Ƶ��ֱ�Ӹ��ƣ�Copy��������ļ�������ζ����Ƶ���ᾭ�����±��룬�Ӷ�����ԭ���ʲ��䡣
# output.m4a ������ļ������������ɵ���Ƶ�ļ�����M4A��ʽ�洢����������Ƶ������ԴFLV�ļ���ȫ��ͬ��





#

