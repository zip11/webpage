<?php

 #写入 关机 到txt
 $handle = fopen("poweroff.txt","w");
 fwrite($handle,"");
 fclose($handle);

 #查看 txt 关机 记录
$file_path = "poweroff.txt";
$str = file_get_contents($file_path);

echo(" 写入 txt关机记录");
echo($str);

if(strncmp("",$str,1)==0){

  echo("清除  成功");
  return("清除成功");

} else {
  echo("清除 失败");
  return("清除 失败");

}


?>



