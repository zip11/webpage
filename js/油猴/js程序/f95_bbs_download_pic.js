// ==UserScript==
// @name         f95zone论坛下载缩略图的大图
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  下载论坛帖子缩略图的大图，download big picture
// @author       0830-2023
// @match        https://f95zone.to/threads/*/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=f95zone.to
// @grant        GM_download
// @grant        GM_notification
// @run-at      document-end
// ==/UserScript==

(function() {

    'use strict';


    //~~~~~~~~~~Add  button3 ~~~~~~~~~~~


    let mybtn = document.createElement('button');

    // 添加 body 按钮，浮动
    document.body.appendChild(mybtn);

    mybtn.id = 'my-btn';
    mybtn.innerHTML = `下载图片
<style>
#my-btn {
    /* position设置为fixed，固定位置，即使窗口滚动位置不变 */
    position: fixed;
    top: 100px;
    left: 30px;
    width: 150px;
}
</style>`

        //  当前-下载图片 个数
        var xzs = 0 ;

    mybtn.onclick = function () {

        // 按钮点击- 下载图片
        // ----start ----

        console.log("big-pic-download_start!");

        // 获取全部大图 网址
        var jpg = document.querySelectorAll(".js-lbImage");



        // 获取 网页元素 数组 元素数量
        var bmnum = jpg.length ;
        console.log("jpg total number:" + bmnum);



        // 获取 当前 时间戳
        var nowtime=new Date().getTime();
        // 时间戳 转 时间 格式
        var nowtimefile = timestampToTime( nowtime);
        console.log("time-now:" + nowtimefile);
        //20200618_10_33_24

        jpg.forEach(element => {

            //  获取 a.href 图片-网址
            var jpgwz1 = element.href

            // console.log("jpg href:" + jpgwz);

            //图片 后缀
            var namhz = picname(jpgwz1);
            // 图片完整文件名
            var picmz1 = nowtimefile + namhz

            // 下载图片 （图片网址，图片名字，图片总数）
            picdown(jpgwz1,picmz1,bmnum);


        }
                   )

        //--- end button ----

    }



    // 下载图片 （图片网址，图片名字，图片总数）
    function picdown(jpgwz,picmz,picnum) {
        // 下载 图片
        GM_download({

            url:jpgwz,
            name: picmz,
            onload: () => {

                //下载数量 +1
                xzs = xzs +1;

                console.log("jpgwz("+ xzs + "):"+jpgwz);

                // 下载完成，提示
                if(picnum <= xzs) {

                    console.log("xz-pic-end:"+xzs);


                    GM_notification({
                        text:"下载结束-下载种子数量:"+xzs,
                        timeout: 2000
                    });
                }


            }

        });

    }

    // 图片 后缀名字
    function picname(nam) {

        let result = nam.lastIndexOf(".");

        let zz = nam.substring(result,);

        return zz;
    }

    // 获取当前时间
    function timestampToTime(timestamp) {

        //var date = new Date(timestamp * 1000);
        var date = new Date(timestamp);
        //时间戳为10位需*1000，时间戳为13位的话不需乘1000

        var Y = date.getFullYear() ;
        var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1):date.getMonth()+1) ;
        var D = (date.getDate()< 10 ? '0'+date.getDate():date.getDate())+ '_';

        var h = (date.getHours() < 10 ? '0'+date.getHours():date.getHours())+ '_';
        var m = (date.getMinutes() < 10 ? '0'+date.getMinutes():date.getMinutes()) + '_';
        var s = date.getSeconds() < 10 ? '0'+date.getSeconds():date.getSeconds();

        return Y+M+D+h+m+s;
    }



})();