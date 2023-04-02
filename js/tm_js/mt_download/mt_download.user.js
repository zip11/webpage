// ==UserScript==
// @name         mt_图片网址保存
// @namespace    mt_download1
// @version      0.1.0
// @description  mt复制下载帖子的图片链接，不同脚本的保存值不通用
// @author       3_30_2023
// @match       https://kp.m-team.cc/adult.php?inclbookmarked=1&allsec=1&incldead=0
// @grant       GM_setClipboard
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        GM_download
// @grant    GM_registerMenuCommand
// @grant    GM_unregisterMenuCommand
// @run-at      document-end
// ==/UserScript==



(function () {

    'use strict';

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
    
    read_menu();

    save_imgsrc();


}) ();