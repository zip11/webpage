<?php

$file_path = "cookie.txt";

if(file_exists($file_path)){

    $str = file_get_contents($file_path);
    //将整个文件内容读入到一个字符串中

    // $str = str_replace("\r\n","",$str);

    $str = 'Cookie: '.$str;

    echo $str;

}
else {
    echo "read cookie.txt error! ";
    exit("read cookie.txt error");
}

?>