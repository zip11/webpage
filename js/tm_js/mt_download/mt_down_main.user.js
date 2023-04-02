// ==UserScript==
// @name         mt-下载种子-删除书签
// @namespace    mt-del-bm
// @version      0.1
// @description  批量下载收藏种子,之后删除种子收藏，测试pt网站的mt站点正常可用，其他网站如果是兼容NexusPHP 站点 ，可以在源码自己添加匹配网址，23-3-18，download torrent,delete bookmark
// @author       zip11guge
// @match        https://kp.m-team.cc/*.php?inclbookmarked=1&allsec=1&incldead=0
// @run-at      document-end
// @grant        GM_download
// @grant       GM_notification
// @grant        GM_setValue
// @grant        GM_getValue
// @grant       GM_setClipboard
// @grant    GM_registerMenuCommand
// @grant    GM_unregisterMenuCommand
// @license      MIT
// ==/UserScript==

(function() {

    'use strict';

    //   @require     file://gh\js\mt-pt\mt.js

    var xzs = 0;



    //~~~~~~~~~~Add 下载种子bookmark button3 ~~~~~~~~~~~


    let mybtn = document.createElement('button');
    document.body.appendChild(mybtn);

    mybtn.id = 'my-btn';
    mybtn.innerHTML = `下载种子bookmark
<style>
#my-btn {
    /* position设置为fixed，固定位置，即使窗口滚动位置不变 */
    position: fixed;
    top: 100px;
    left: 30px;
    width: 150px;
}
</style>`

        // download torrent ~ start ~~~~~~~~~~~~~~~~~~~~~
    mybtn.onclick = function () {

        //输入-开始 download pic-link

        let wz1 = GM_getValue("imgurl1")
        console.log("imgurl1",wz1)
    
        let wz2 = GM_getValue("imgurl2")

        let ks1 = wz1;
        let js1 = wz2;
        
        // let ks1 = prompt("输入-第一个收藏的-图片链接-pic-link");

        //let js1 = prompt("输入-最后一个收藏的-图片链接pic-link");

        //网址 转换到数字--st---
        let bknum = ckimg(ks1);

        console.log("bknum-st:"+bknum);

        // 输入-结束 download pic-link    
        console.log(js1);

        //网址 转换到数字
        let bknum_ed = ckimg(js1);

        console.log("bknum-ed:"+bknum_ed);
        
        //--end---

        // download
        // 统计下载数量，计算完成所有任务
        var xzs = bknum;

        down_torrent(bknum,bknum_ed);

        //del bookmark
        delbm(bknum,bknum_ed);
        


        GM_notification({
            text:"种子下载开始-torrent download num"+bknum_ed,
            timeout: 2000
        });

        //alert("种子下载开始-torrent download start");

    }



    // 异步 延时 秒
    function sleep1(time) {

        time*=1000
        return new Promise(resolve => {
            setTimeout(() => {
                resolve();
            }, time);
        });
    }

    // menu---st
    
    function read_menu(){

        let id=GM_registerMenuCommand ("read-value-console", function(){
        

            let wz1 = GM_getValue("imgurl1")
            console.log("imgurl1",wz1)
        
            let wz2 = GM_getValue("imgurl2")
            console.log("imgurl2",wz2)
    
            //GM_unregisterMenuCommand(id);//删除菜单
        }, "h");
    }

    // end ----

    // 保存 点击-种子缩略图-网址
    function save_imgsrc() {

        var imgnum = 0;
        //图片的网址 数量
        
    
    
        let rs = document.querySelectorAll(".torrentimg > a ")
        // css选择 收藏种子→，种子 缩略图片上的 a链接
    
        rs.forEach(element => {
    
            console.log(element.src);
            // a src
            
            // 修改打开网页 为 复制 缩略图 网址
            element.addEventListener('click',(e)=>{
            
                //ddEventListener方法用于向指定元素添加事件句柄
                
                e.preventDefault();
                // 取消该click 默认事件
                
                let imgurl = e.target.src;
                
                console.log("a.click",imgurl);
                // target 事件属性返回触发事件的元素。
                
                GM_setClipboard(imgurl);
                //复制 文本 到剪贴板
                
                imgnum = imgnum +1;
                // 网址计数 +1
    
                console.log("imgnum:",imgnum)
    
                // 保存 图片 网址
                switch (imgnum) {
    
                    case 1:
                        GM_setValue("imgurl1",imgurl);
                        break;
                    case 2:
                        GM_setValue("imgurl2",imgurl)
                        imgnum = 0 ;
                        break;
                        // 第二个网址 ，清零网址 次数计数
                    
                }
    
    
            
            })
    
        })
    }
    



    // 下载种子文件---st----

    async function down_torrent(qdnum,bmnum){

        var i;

        // bookmark start num
        // qdnum

        // bookmark end num


        //var bmnum = tp1.length

        var xy1 = null

        for (i = qdnum; i <= bmnum ; i++) {

            xy1 = document.querySelector('a[id="bookmark'+ i + '"]').previousElementSibling;
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

            // 异步延时-sleep
            await sleep1(3);

            // download  .torrent


            console.log("xz-qd-num:"+ xzs);

            GM_download({

                url:xy1.href,
                name:tmz1,
                onload: () => {

                    //下载数量 +1
                    xzs = xzs +1;

                    // 下载完成，提示
                    if(bmnum < xzs) {
                        console.log("xz-end:"+xzs);


                        GM_notification({
                            text:"下载结束-下载种子数量:"+xzs,
                            timeout: 2000
                        });
                    }


                }

            });




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





    // del mt bookmark ---start---

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


    read_menu();
    // 读取 图片缩略图 网址

    save_imgsrc();
    // 保存 点击种子缩略图-网址

})();

