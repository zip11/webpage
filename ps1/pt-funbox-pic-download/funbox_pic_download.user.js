// ==UserScript==
// @name         下载趣味盒的图片
// @namespace    download-funbox-pic
// @version      0.1.2
// @description  下载pt网站的趣味盒的图片,兼容 NexusPHP 的网站,点击网页中的 下载趣味盒图片 按钮，游览器开始下载所有图片，默认下载原始文件名图片，修改选项，可用下载txt链接文件，用以使用第三方下载软件，适合大文件下载，不容易下载失败且速度快，24-02-15
// @author       zip11
// @match        https://*/fun.php?action=view
// @grant       GM_download
// @grant       GM_notification
// @grant       GM_setValue
// @grant       GM_getValue
// @grant       GM_registerMenuCommand
// @grant       GM_unregisterMenuCommand
// @grant       GM_setClipboard



// @license      MIT
// ==/UserScript==
/* ==UserConfig==
group1:

  configC: 
    title: 图片文件名_序号_原始文件名
    description: 图片_原始文件名，number数字序号_图片名字
    type: select
    default: yuanshi
    values: [yuanshi,number]

  configB:
    title: 是否下载图片
    description: 默认下载图片，否则只复制链接
    type: checkbox
    default: true

 ==/UserConfig== */

 (function() {

    'use strict';

    // 菜单 设置图片文件名 数字序号---

    var pzname = GM_getValue("group1.configC")

    console.log("pzname=" + pzname);


    // ---end ---- 


    // BUTTON 5
    var button5 = document.createElement("button");

    button5.id = "id005";
    button5.textContent = "下载趣味盒图片";
    button5.style.width = "140px";
    button5.style.height = "20px";
    button5.style.align = "center";

    // END ~~~~~~~~

    // 按钮点击
    button5.onclick = function (){

        // 读取 是否下载配置
        let copy_or_down = GM_getValue("group1.configB")

        if (copy_or_down == true){

            msgk("开始下载任务");
            picsnap();
        } else {
            
            // 复制图片链接，到剪贴板
            let file_down = copy_pic_link();
            downloadStringAsFile(file_down, "links.txt");

        }

   
    };

    //~~~~~~~~~~Add Button ~~~~~~~~~~~

    //查找  上一页的 元素
    var x = document.querySelector("body");

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("button 对象:",x);

    //添加 子元素
    //x.appendChild(button5);

    //insertBefore
    x.parentNode.insertBefore(button5, x);

    //~~~~~~~~~end~~~~~~~


        // 定义一个下载字符串的函数
    function downloadStringAsFile(str, fileName) {
        // 创建一个Blob对象，包含要下载的字符串
        var blob = new Blob([str], { type: 'text/plain;charset=utf-8' });

        // 创建一个临时的a元素
        var tempLink = document.createElement('a');

        // 设置a元素的href属性为Blob对象的URL
        tempLink.href = URL.createObjectURL(blob);

        // 设置a元素的download属性为文件名
        tempLink.download = fileName;

        // 触发a元素的点击事件，开始下载
        tempLink.click();

        // 释放Blob对象的URL
        URL.revokeObjectURL(tempLink.href);
    }




    // css选择图片网址，下载图片
    function picsnap() {

        console.log('点击了按键,复制funbox img');

        // button5 text
        // var p=document.getElementById("id005");
        // p.innerHTML="开始下载";

        //var dmmimg=document.getElementsByName("funbox");

        // 获取 所有图片 元素
        let funimg=document.querySelectorAll("img");
        


        // 图片数量
        let i;

        // var img name
        let mz1='';

        // var img total number
        let imgnum = funimg.length;

        // button5 text
        //p.innerHTML="num="+imgnum;

        // 循环 下载 图片
        for (i = 0; i < imgnum ; i++) {

            // jpg src
            let picdt = funimg[i].src;
            console.log("jpg-src:"+picdt);

            // jpg name
            mz1 = GetPageName(picdt);

            // 判断 -图片文件名-数字序号
            let wjnum = GM_getValue(pzname)

            if (wjnum == "number") {

                // 获取 文件 后缀
                let suffix = mz1.substring(mz1.lastIndexOf("."));
                // 数字序号 名字
                mz1 = i + suffix;
            }
            // ---end---

            // 下载图片 数量 统计---st---
            // no-down-img-number
            let nodown_img = imgnum - i ;

            // 按钮文本 修改 为 下载图片 剩余数量
            //p.innerHTML="num="+nodown_img;
            console.log("pic-num:" + nodown_img );
            
            // 下载图片
            down_jpg(picdt,mz1,i,imgnum);


        }
        // pic num = 0
        // p.innerHTML="num=0";
    }

    // 复制图片链接 ，到剪贴板，txt下载
    function copy_pic_link() {

        // 获取 所有图片 元素
        let dx = document.querySelectorAll("img");

        let pic_link = '';
        // 遍历dx
        for (let i = 0; i < dx.length; i++) {

            // 获取 图片链接
            let ljtp = dx[i].src;
            
            // 生成 txt 单行，图片链接
            pic_link = pic_link + ljtp + "\n";
        
        }

        GM_setClipboard(pic_link);
        
        const endt = " 复制图片链接 ，到剪贴板，下载txt，完成";
        console.log(endt);
        msgk(endt);

        return pic_link;
        
    }

    // 下载图片
    function down_jpg(ljtp,mz2,xzs,bmnum) {

        // download jpg

        GM_download({

            url:ljtp,
            name:mz2,
            onload: () => {

                // 下载完成，提示
                xzs = xzs +1;
                if(xzs >= bmnum) {
                    console.log("xz-end:"+xzs);


                    msgk("下载结束-下载种子数量:"+xzs);

                }
                else {
                    console.log("xz-num:"+xzs+"/total_num:"+bmnum);
                }


            }

        });


    }

    // msgbox 4s
    function msgk(wb1) {

        GM_notification({
            text:wb1,
            timeout: 4000
        });       
    }

    //获取url 文件名
    function GetPageName(url)
    {

        var tmp= [];//临时变量，保存分割字符串

        tmp=url.split("/");//按照"/"分割

        var pp = tmp[tmp.length-1];//获取最后一部分，即文件名和参数

        //tmp=pp.split("?");//把参数和文件名分割开

        return pp;
    }

})();