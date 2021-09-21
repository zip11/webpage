<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>yt-dl下载</title>
  <!--利用cdn添加js和css库  -->
  <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>

</head>
  <body>

    <p>Enter video link here:</p>

    <form method="post" action='save.php'>

      <textarea cols = "150" rows = "20" wrap = "soft"  name = "textareaValue" id = "wz2">
      
      </textarea>

      <ul>
          <li><input type ="checkbox" name ="category[]" value = 1>中文 字幕 下载vtt</li>
          <li><input type ="checkbox" name ="category[]"  value = 2>播放列表 下载</li>
          <li><input type ="checkbox" name ="category[]" value = 3>播放列表 中文字幕 下载</li>
          
      </ul>


      <input type="submit" value="Enter" />
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

            var name = $("#wz2").val();
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

