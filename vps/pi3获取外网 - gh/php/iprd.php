<?php

//	读取文件
$myfile = fopen("ip.txt", "r") or die("Unable to open file!");

echo fread($myfile,filesize("ip.txt"));

fclose($myfile);

?>
