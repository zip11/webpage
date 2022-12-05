<?php
  
    function discuz_sign(){
        
        function get_response($url,$cookie)
        {
              $curl = curl_init(); 
                curl_setopt($curl, CURLOPT_URL, $url);
                curl_setopt($curl, CURLOPT_HEADER, 0);
                curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
                curl_setopt($curl,CURLOPT_COOKIE,$cookie);
                curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); 
                curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);  
                $response = curl_exec($curl);  
                curl_close($curl);
                return $response;
            
        }
        
        $link = 'https://bbs.tampermonkey.net.cn/plugin.php?id=dsu_paulsign:sign';
        $cookie = 'cookie:';
        $response = get_response($link,$cookie);
        
        preg_match_all('<input type="hidden" name="formhash" value="(.*?)" />', $response, $match);
        $formhash = $match[1][0];
        
        $result = get_response($link . '&operation=qiandao&inajax=1&qdxq=kx&qdmode=2&todaysay=&fastreply=1&formhash=' . $formhash,$cookie);
        
        echo $result;
    }
?>