// ==UserScript==
// @name         ptt_title_copy
// @namespace    ptt_title_copy2
// @version      0.1.0
// @description  ptt_title_copy1_clipboard
// @author       10-1-2023
// @match        https://www.pttime.org/details.php?id=*
// @grant        GM_setClipboard
// ==/UserScript==

(function() {
    'use strict';

    // 下载文件 标题
    let file_title = document.querySelector("#top").textContent

    console.log("ptt-title-copy:"+file_title)

    let str = file_title;

    // 标题 删除[] ~~~~~~start~~~~~~~~

    // 搜索 字符串 [
    let zfwz = str.indexOf("[");

    // 分割 字符串
    str = str.slice(0,zfwz);

    console.log("del [] after string:"+str);

    GM_setClipboard(str);

    // [] 正则提取困难
    // var reg1 = new RegExp("\[.*]","g"); // 加'g'，删除字符串里所有的"a"
    // var a1 = str.replace("/\[.*]/g","")
    // console.log(a1); // bbccddeegg

})();

