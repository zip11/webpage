<?php


//post传入  mysql插入 数据

$post_str = $_POST['wz4'];//获取索引值

//读取cookie mysql上次 读取 字段 位置

if (isset($_COOKIE["user"])){

    echo "读取记录cookie " . $_COOKIE["user"] . "!<br>";
    $sz=$_COOKIE["user"]+1;
    setcookie("user",$sz , time()+3600);

}
else{

    echo "创建 读取 mysql记录!<br>";
    setcookie("user","0" , time()+3600);

}

$wz9 = $_COOKIE["user"];
$wz9 = (int)$wz9;
echo  'sql wz :' . $wz9;
//----end   

// 假定数据库用户名：root，密码：123456，数据库：myDBPDO

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

//--end

//cookie 记录 <=  读mysql数据的多少行  
if ($wz9 < $rowcount){

    //     选择 列                选择 表
    $sql="SELECT firstname  FROM MyGuests ";

    if ($result=mysqli_query($con,$sql))
    {
        //查找行号为 2 的数据  $wz9
        mysqli_data_seek($result,$wz9);
        
        // 读取数据
        $row=mysqli_fetch_row($result);
        
        printf ("name: %s ", $row[0]);
        
        //写磁力链接
        $cili = base64_encode($row[0]);
        setrawcookie("magent",$cili, time()+3600);
        
        // 释放结果集
        mysqli_free_result($result);
    }

}
else{

    echo '读取mysql 已经到末尾,没有数据';

    //sql 读取位置 记录，归零
    setcookie("user","0" , time()+3600);

    //clear magent
    setrawcookie("magent","", time()+3600);

}





mysqli_close($con);



?>