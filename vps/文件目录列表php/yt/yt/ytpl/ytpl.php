<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>yt-dl下载</title>
  <!--利用cdn添加js和css库  -->
  <script src="resources/themes/bootstrap/js/jquery.min.js"></script>

</head>
  <body>

    <p>Enter video link here:</p>

    <form action ="HandleFormCheckBox.php" method="post">

        <ul>

          <li><input type ="checkbox" name ="category[]" value = 4>txt批量 下载</li>
          <li><input type ="checkbox" name ="category[]" value = 1>中文字幕 下载</li>
          <li><input type ="checkbox" name ="category[]"  value = 2>播放列表 下载</li>
          <li><input type ="checkbox" name ="category[]" value = 3>播放列表 中文字幕 下载</li>

        </ul>

        播放列表 id(网址后 &list= ): <input type="text" name="listid">
        播放列表 开始序号: <input type="text" name="liststart">
        播放列表 结束序号: <input type="text" name="listend1">

        <input type ="submit">

    </form>



    <button id="send">写入txt</button>


    <button id="send1">多选 判断</button>

    <div id="result">txt网址记录:</div>

    <?php

      $file_path = "newfile.txt";
      $str = file_get_contents($file_path);
      echo($str);

    ?>


  </body>


  <script type="text/javascript">
 
 $(function () {
     $("#send1").click(function () {

         var name = $("#wz2").val();
         var data = "wz4="+name; //如果后台是$_POST方法获取数据，那么一定要索引（例如：索引name）

           $.ajax({
             type: "POST",
             url: "HandleFormCheckBox.php",  //同目录下的php文件

           success: function(msg){  //请求成功后的回调函数
             
               $("#result").append(msg);

           }
       });

     })
 })

</script>

  <script type="text/javascript">
 
    $(function () {
        $("#send").click(function () {

            var name = $("#wz4").val();
            var data = "wz4="+name; //如果后台是$_POST方法获取数据，那么一定要索引（例如：索引name）

              $.ajax({
                type: "POST",
                url: "server.php",  //同目录下的php文件
                data:"wz4="+name,  // 等号前后不要加空格
              success: function(msg){  //请求成功后的回调函数
                
                  $("#result").append(msg);

              }
          });

        })
    })

  </script>
</html>

