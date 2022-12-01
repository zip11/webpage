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