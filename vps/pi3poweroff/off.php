<?php

 #写入 关机 到txt
 $handle = fopen("poweroff.txt","w");
 fwrite($handle,"poweroff");
 fclose($handle);

 #查看 txt 关机 记录
$file_path = "poweroff.txt";
$str = file_get_contents($file_path);

echo(" 写入 txt关机记录");
echo($str);

if(strncmp("poweroff",$str,8)==0){

  echo("写入成功");
  return("写入成功");

} else {
  echo("写入 失败");
  return("写入 失败");

}


?>



