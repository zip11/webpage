// ==UserScript==
// @name         bilibili_video_link
// @namespace    download_video_link
// @version      0.1.0
// @description  bilibili获取视频列表，视频链接网址
// @author       20240129
// @match        https://space.bilibili.com/*
// @grant        GM_setClipboard
// @grant       GM_notification
// @require     https://scriptcat.org/lib/513/2.0.0/ElementGetter.js


// ==/UserScript==

// 获取 bilibili视频列表 ，所有视频链接

function getElementsByClass(className) {
    return document.getElementsByClassName(className);
}



/*
let ops = document.querySelector("#arc_toolbar_report .ops");
ops.addEventListener("DOMNodeInserted", function (event) {
    //触发了dom插入

    lj();
});
*/

(function() {

    console.log("等待视频图片-加载！！！");

    // 等待 视频背景 ，小图片
    elmGetter.get('[class="fake-danmu-mask"]').then(div => {
        
        console.log("视频图片-加载-完成！！！");
        check_link();
    });

})();

// 获取 视频链接
function check_link() {

    // 获取具有 "title" 类的所有元素
    var elements = getElementsByClass("title");

    let vname = [];
    let vlink = [];

    // 遍历所有具有 视频标题 类的元素
    for (let i = 0; i < elements.length; i++) {
        
        vname.push(elements[i].title);
        vlink.push(elements[i].href);

    }
    // end ~~~~~~~~~~~~~~~~

    // 复制剪贴板 -格式
    var endtext = ""
    for (let i = 0;i < vname.length; i++) {

        endtext = endtext + '\#' + vname[i] + "\#\n";
        endtext = endtext + vlink[i] + "\n";
    }

    // 使用正则表达式替换 ##|undefined
    endtext = endtext.replace(/##|undefined/g, '');

    GM_setClipboard(endtext);
    // 将数据复制到剪贴板


    // 截取 字符串 30个字符
    let msgtext = endtext.substring(0,29);

    // 消息框
    GM_notification({
        title: location.host,
        text: msgtext,
        timeout: 5000,
        highlight: false,
        
    });
}
