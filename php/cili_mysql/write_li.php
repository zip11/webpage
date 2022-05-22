<?php

//post传入  mysql插入 数据

//获取  magent
$post_str = $_POST['name'];
echo 'post magent' . $post_str . '<br>';

// 文件名字
$post_url = $_POST['url'];
echo 'post url ' . $post_url . '<br>';

$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "myDBPDO";

try {
    
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    
    // 设置 PDO 错误模式，用于抛出异常
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    //插入 数据
    $sql = "INSERT INTO MyGuests (firstname,lastname)
    VALUES ('$post_str','$post_url')";
    
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