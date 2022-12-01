### javascript XMLHttpRequest实现下载文件 ###
[https://blog.csdn.net/sunct/article/details/90106429](https://blog.csdn.net/sunct/article/details/90106429)


// @grant        GM_xmlhttpRequest
// @connect      *


@connect *”表示允许任何域名的跨域请求。当然，我们这里写成“@connect 192.168.0.109”也是可以的


Greasemonkey用的是GM.xmlHttpRequest，Tampermonkey用的是GM_xmlhttpRequest

            GM_xmlhttpRequest ( {
                method:     "GET",
                url:        xy1.href,
                onload:     function (response) {
                    console.log(response.responseText);


                },
                onerror:    function (){
                    alert('连接失败');
                }
            } );


                        onload: function(res){
                            if(res.status === 200){
                                console.log('成功')
                            }else{
                                console.log('失败')
                                console.log(res)
                            }
                        },
                        onerror : function(err){
                            console.log('error')
                            console.log(err)
                        }
————————————————
版权声明：本文为CSDN博主「颓宝」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/chirenshuomeng1/article/details/103011165