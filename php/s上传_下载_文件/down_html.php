<?php
// 文件的URL地址
$url = 'http://192.168.2.1';

// 使用file_get_contents获取文件内容
$file_content = file_get_contents($url);

// 如果文件内容获取成功
if ($file_content !== false) {
    // 设置HTTP响应头，告诉浏览器这是一个文件下载
    header('Content-Type: text/html');
    header('Content-Disposition: attachment; filename="daohang.html"');

    // 输出文件内容
    echo $file_content;
    exit;
} else {
    // 如果文件内容获取失败，输出错误信息
    echo 'Error: Unable to download the file.';
}
?>