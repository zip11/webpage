<?php
    exec('youtube-dl   -a  /var/www/dl/wj/yt/newfile.txt   -f "[height<=720][tbr<1999]"  -o "/var/www/dl/wj/yt/phvideo/%(title)s.%(ext)s" ',$result);
    print_r($result);
?>  