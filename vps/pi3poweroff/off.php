<html>

<head>
<meta charset="UTF-8">

<title>简单时长倒计时</title>

<SCRIPT type="text/javascript">
            var maxtime = 60 ; //一个小时，按秒计算，自己调整!
            function CountDown() {
                if (maxtime >= 0) {
                    
                    // minutes = Math.floor(maxtime / 60);
                    seconds = Math.floor(maxtime);
                    msg = "距离结束还有" + seconds + "秒";
                    
                    document.all["timer"].innerHTML = msg;
                    

                        --maxtime;
                } else{
                    clearInterval(timer);
                    alert("时间到，结束!");
                }
            }
            timer = setInterval("CountDown()", 1000);
</SCRIPT>

</head>

<body>

<div id="timer" style="color:red"></div>
<div id="warring" style="color:red"></div>


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

</body>

</html>



