<?php
    exec('yt-dlp   -a  /var/www/dl/wj/yt/newfile.txt  -f 22/18  -o "/var/www/dl/wj/yt/video/%(title)s.%(ext)s" ',$result);
    print_r($result);
?>  