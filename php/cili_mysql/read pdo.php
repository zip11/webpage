<?php



    $dsn  = 'mysql:host=127.0.0.1;dbname=myDBPDO';
    $user = 'root';
    $pwd  = '123456';

    try{
        $pdo = new PDO($dsn,$user,$pwd);
        $sql = 'SELECT firstname FROM MyGuests ';
        $res = $pdo -> query($sql);
        echo '<pre>';
        $row = $res -> fetch(PDO::FETCH_ASSOC, PDO::FETCH_ORI_ABS, 1);
            print_r($row);
            print_r($row['firstname']);
        
    }catch(PDOException $e){
        echo '数据库连接失败：'.$e -> getMessage();
    }

    $conn = null;


?>

