
<?php
 


    $username = $_POST['wz4'];//获取索引值
    
    //echo  $username;

    $file_path = "newfile.txt";
    ini_set("error_reporting", E_ALL);

    #echo $_POST["textareaValue"];

    #写入 网址 到txt
    $handle = fopen("newfile.txt","w");
    fwrite($handle,$username);
    fclose($handle);

    $str = file_get_contents($file_path);

    //echo $str;

    $result = "ok ajaxx";

    return "ok-ajax";





?>

