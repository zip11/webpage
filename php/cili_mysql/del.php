<?php

// mysql del table

$servername = "localhost";
$username = "root";
$password = "123456";
$dbname = "myDBPDO";
 
// 创建连接
$con = mysqli_connect($servername, $username, $password, $dbname);


// 检测连接
if (mysqli_connect_errno())
{
    echo "连接失败: " . mysqli_connect_error();
}

mysqli_query($con,"DELETE FROM MyGuests ");

mysqli_close($con);

echo 'sql del table ok ';

?>