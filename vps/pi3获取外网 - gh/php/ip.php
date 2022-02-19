<?php

$iipp = $_SERVER["REMOTE_ADDR"];

echo $iipp ;

$myfile = fopen("ip.txt", "w") or die("Unable to open file!");

$txt = $iipp;

fwrite($myfile, $txt);

fclose($myfile);

?>
