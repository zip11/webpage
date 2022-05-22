
<?php
 
     //post传入  mysql插入 数据

    $post_str = $_POST['wz4'];//获取索引值
    
    echo 'post ' . $post_str . '<br>';

    $servername = "localhost";
    $username = "root";
    $password = "123456";
    $dbname = "myDBPDO";
     
    try {
        
        $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
        
        // 设置 PDO 错误模式，用于抛出异常
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        //插入 数据
        $sql = "INSERT INTO MyGuests (firstname)
        VALUES ('$post_str')";
        
        // 使用 exec() ，没有结果返回 
        $conn->exec($sql);
        
        echo "新记录插入成功";
    
    }
    catch(PDOException $e)
    {
        echo $sql . "<br>" . $e->getMessage();
    }
     
    $conn = null;


?>

