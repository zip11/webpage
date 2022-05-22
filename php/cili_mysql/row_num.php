<?php 

// 假定数据库用户名：root，密码：123456，数据库：RUNOOB 
$con=mysqli_connect("localhost","root","123456","myDBPDO"); 

if (mysqli_connect_errno($con)) 
{ 
    echo "连接 MySQL 失败: " . mysqli_connect_error(); 
} 

//     选择 列                选择 表
$sql="SELECT firstname  FROM MyGuests ";

if ($result=mysqli_query($con,$sql))
{
    // 返回记录数
    $rowcount=mysqli_num_rows($result);
    printf("总共返回 %d 行数据。",$rowcount);
    // 释放结果集
    mysqli_free_result($result);
}


mysqli_close($con);
?>