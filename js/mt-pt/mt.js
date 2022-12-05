

(function() {

    'use strict';

    //   @require     file://D:\github\webpage\js\mt-pt\mt.js

    // download torrent ~ start ~~~~~~~~~~~~~~~~~~~~~
    var button3 = document.createElement("button");

    //按钮 属性
    button3.id = "id003";
    button3.textContent = "下载种子bookmark";
    button3.style.width = "140px";
    button3.style.height = "20px";
    button3.style.align = "center";

    //~~~~~~~~~~Add button3 ~~~~~~~~~~~

    //查找  上一页的 元素
    var b3 = document.getElementsByClassName('gray')[0];

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("button3 对象:",b3);

    //添加 子元素
    b3.appendChild(button3);

    button3.onclick = function (){

        //输入-开始 download pic-link

        let ks1 = prompt("输入-开始收藏-pic-link");
        let bknum = ckimg(ks1);

        console.log("bknum-st:"+bknum);

        // 输入-结束 download pic-link

        let js1 = prompt("输入-结束pic-link");
        console.log(js1);
        let bknum_ed = ckimg(js1);

        console.log("bknum-ed:"+bknum_ed);

        // download
        down_torrent(bknum,bknum_ed);

        //del bookmark
        delbm(bknum,bknum_ed);
    }

    function down_torrent(qdnum,bmnum){

        var i;

        // bookmark start num
        // qdnum

        // bookmark end num


        //var bmnum = tp1.length

        var xy1 = null

        for (i = qdnum; i <= bmnum ; i++) {

            xy1 = document.querySelector('a[id="bookmark'+ i + '"]').previousElementSibling;;
            // css选择 收藏 bookmark (上一个元素 a )下载连接

            console.log("torrent-link:"+xy1.href);
            // 收藏网址

            // torrent name -------
            // title    parent > previous
            let wztt = xy1.parentNode.previousElementSibling;
            // firstChild dom
            wztt = wztt.firstChild;

            console.log(wztt.title);

            // a > title
            let tmz1 = wztt.title
            // titele  abc-123
            tmz1 = tmz1.replace(/[^a-zA-Z0-9-]/g,'')


            tmz1 = "[M-TEAM]" + tmz1 + ".torrent";
            // torrent name  end ------

            //点击 下载 收藏

            // download  .torrent
            GM_download(xy1.href,tmz1);


        }
    }

    // ~~~~~~button3~~~~~~ end




    // check bookmark number----start

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

    // ~~~~~~~~end button2 ~~~~~~~~~~~~



    // ~~~ Button ~~~~ delete bookmark---- start

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


        //输入-开始 del download pic-link

        let ks1 = prompt("输入-开始收藏-pic-link");
        let bknum = ckimg(ks1)

        console.log("bknum-st:"+bknum);

        // 输入-结束 del download pic-link

        let js1 = prompt("输入-结束pic-link");
        console.log(js1);
        let bknum_ed = ckimg(js1)

        console.log("bknum-ed:"+bknum_ed);

        // delete bookmark

        delbm(bknum,bknum_ed)

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

        for (i = qdnum; i <= bmnum ; i++) {

            var xy1 = document.querySelector('a[id="bookmark'+ i + '"]');
            //css选择 全部 收藏 bookmark

            console.log(xy1.href);
            // 收藏网址

            xy1.click();

            //点击 删除 收藏
        }
    }

})();

