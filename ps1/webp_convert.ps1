# $PSDefaultParameterValues['*:Encoding'] = 'utf8'


# ��ʾ�û������ļ���·��
$folderPath = Read-Host "���������JPG�ļ����ļ���·��"

# pic 
$pic_ext = "webp"

# ���� jxl ���ļ���
$jxlfolder = $folderPath + "_" + $pic_ext
New-Item -ItemType Directory -Force -Path $jxlFolder | Out-Null
write-host "�Ѵ��� _jxl �ļ���,$jxlFolder"

# ����ָ���ļ���������jpg�ļ�
Get-ChildItem -Path $folderPath -Filter *.jpg -Recurse | ForEach-Object {

    # ��ȡ��ǰjpg�ļ�������·��
    $jpegFile = $_.FullName

    # ��������ļ�������������ͬĿ¼��ֻ�ı���չ��Ϊ.jxl��
    # $jxlFile = $jxlFolder + "\" + $_.BaseName + ".jxl"

    # ��������ļ�������������ͬĿ¼��ֻ�ı���չ��Ϊ.jxl��
    $jxlFile = $jxlfolder + "\" + $_.BaseName + "." + $pic_ext

    # ʹ��cjxl�����������ת��
    # & "D:\Program Files\libjxl\cjxl.exe" $jpegFile $jxlFile

    # webp q=75
    ffmpeg -i "$jpegFile" -vf scale=-2:4320 -c:v libwebp -q:v 75  "$jxlFile"
    
    write-host "ת�� $jpegFile => $jxlFile"
}

Write-Host "ת����ɣ�"

Pause