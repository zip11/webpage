<html>
  <body>

    <p>Enter video link here:</p>

    <form method="post" action='save.php'>

      <textarea cols = "150" rows = "20" wrap = "soft" id = "story" 
       name = "textareaValue">
      
      </textarea>
      <input type="submit" value="Enter" />
    </form>


    <p>txt网址记录:</p>

    <?php

    $file_path = "newfile.txt";
    $str = file_get_contents($file_path);
    echo($str);

    ?>


  </body>
</html>

