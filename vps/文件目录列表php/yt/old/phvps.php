<?php
    exec('youtube-dl   -a  /var/www/dl/wj/yt/newfile.txt   -f 720p/480p   -o "/var/www/dl/wj/yt/phvideo/%(title)s.%(ext)s" ',$result);
    print_r($result);
?>  