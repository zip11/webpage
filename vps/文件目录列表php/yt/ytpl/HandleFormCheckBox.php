<?php

$snum = 0;

$checkbox_select=$_POST["category"];

for($i=0;$i<count($checkbox_select);$i++)

{

  echo "选项".$checkbox_select[$i]."被选中<br />";
  
  $snum = $checkbox_select[$i] + $snum;

}

echo $snum.'<br />';
#计算 总数 




//yt-dl下载

$ytml = 'youtube-dl   -a  /var/www/dl/wj/yt/newfile.txt  -f 22/18  -o "/var/www/dl/wj/yt/video/%(title)s.%(ext)s" ';
    
#yt 自动 生成 字幕 中文
$ytzm = ' --write-auto-sub  --sub-lang zh-Hans  ';


#播放 列表 下载


$lissta = $_POST['liststart'];
$lisend1 = $_POST['listend1'];
$listid = $_POST['listid'];

$ytpl = 'youtube-dl -f 22/18 -i --playlist-start ';
$ytpl2 = ' --playlist-end ';


if($snum == 1){

  #中文 字幕 下载
  $ytml = $ytml.$ytzm;
  echo $ytml;

}elseif($snum == 2) {

  $ytml = $ytpl.$lissta.$ytpl2.$lisend1." ".$listid;
  echo $ytml;


}elseif($snum ==3) {

  $ytml = $ytpl.$lissta.$ytpl2.$lisend1." ".$listid.$ytzm;
  echo $ytml;

}elseif($snum == 4) {

  $ytml = $ytml;
  echo $ytml;
  
}




exec($ytml,$result);

print_r($result);


?>









<!-- <?php

$checkbox_select=$_POST["category"];
print_r($checkbox_select);

?> -->

