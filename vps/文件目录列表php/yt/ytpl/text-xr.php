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

    <form method="post" action='save.php'>

      <!-- #输入 网址 -->

      <textarea cols = "150" rows = "20" wrap = "soft"  name = "textareaValue" id = "wz4">
      
      </textarea>

      <input type="submit" value="写入txt form" />

    </form>


    <button id="send">写入 txt ajax</button>

    
    <a href="ytpl.php" target="_blank">yt txt批量 下载</a>

    <div id="result">txt网址 记录:</div>


    <!-- #读取 网址 txt -->

    <?php

      $file_path = "newfile.txt";
      $str = file_get_contents($file_path);
      echo($str);

    ?>


  </body>

  <!-- ajax 写入 网址 txt -->

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

