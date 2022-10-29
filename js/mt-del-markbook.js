(function() {

    'use strict';

    // check bookmark number

    var button2 = document.createElement("button");

    //按钮 属性
    button2.id = "id002";
    button2.textContent = "查询bookmark序号";
    button2.style.width = "140px";
    button2.style.height = "20px";
    button2.style.align = "center";

    //~~~~~~~~~~Add Button2 ~~~~~~~~~~~

    //查找  上一页的 元素
    var b2 = document.getElementsByClassName('gray')[0];

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("button2 对象:",b2);

    //添加 子元素
    b2.appendChild(button2);

    //~~~~~~~~~end~~~~~~~

    button2.onclick = function (){

        //输入-开始删除收藏-序号
        var ks1 = prompt("输入-img-link*");
        console.log(ks1);

        // input img.src ,serach bookmark number
        var bknum = ckimg(ks1)
        
        //alert(bknum)
        
        // input = book  mark number

        var ip1 = document.querySelector("#searchinput")
        ip1.value = bknum
    }

    // check img number

    function ckimg(imglk) {

        //css选择 全部 小缩略图
        var tp1 = document.querySelectorAll('.torrentimg>a>img');
        
        // img number
        console.log("img number:"+tp1.length)

        var i;

        // bookmark start num
        // qdnum

        // bookmark end num
        
        var bmnum = tp1.length

        

        for (i = 0; i < bmnum ; i++) {


            //console.log("img.src: "+tp1[i].src);

            // 收藏网址

            //输入网址 = 查询网址
            if(imglk == tp1[i].src) {

                //得到 bookmark 编号
                console.log("img.src: "+tp1[i].src);
                return i
            }


        }
    }

    // ~~~~~~~~

    // ~~~ Button ~~~~ delete bookmark

    var button = document.createElement("button");

    //按钮 属性
    button.id = "id001";
    button.textContent = "删除收藏";
    button.style.width = "120px";
    button.style.height = "20px";
    button.style.align = "center";



    //~~~~~~~~~~Add Button ~~~~~~~~~~~

    //查找  上一页的 元素
    var x = document.getElementsByClassName('gray')[0];

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("button 对象:",x);

    //添加 子元素
    x.appendChild(button);

    //~~~~~~~~~end~~~~~~~

    button.onclick = function (){

        //输入-开始删除收藏-序号
        var ks1 = prompt("输入-开始删除收藏-序号bookmark*");
        console.log(ks1);

        //输入-结束删除收藏-序号
        var js1 = prompt("输入-结束删除收藏-序号");
        console.log(js1);

        // delete bookmark
        delbm(ks1,js1)

    }





    function delbm(qdnum,bmnum) {

        // delete bookmark

        var tp1 = document.querySelectorAll('.torrentimg');
        //css选择 全部 小缩略图
        console.log("img number:"+tp1.length)

        var i;

        // bookmark start num
        // qdnum

        // bookmark end num


        //var bmnum = tp1.length

        for (i = qdnum; i < bmnum ; i++) {

            var xy1 = document.querySelector('a[id="bookmark'+ i + '"]');
            //css选择 全部 收藏 bookmark

            console.log(xy1.href);
            // 收藏网址

            xy1.click();
            //点击 删除 收藏
        }
    }

})();