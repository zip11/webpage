// ==UserScript==
// @name         百度热搜_点击转_复制
// @namespace    baidu_click1
// @version      0.1.0
// @description  百度热搜 -点击劫持
// @author       2023年3月30日
// @match        https://www.baidu.com/
// @grant        GM_log
// @grant        GM_setClipboard
// ==/UserScript==



GM_log("baidu_click-start!!!", "info");

// css选择 热搜标题
let rs = document.querySelectorAll(".title-content-title")
    
rs.forEach(element => {
    
    console.log(element);
    GM_log(String(element.innerHTML));

    element.addEventListener('click',(e)=>{

        //ddEventListener方法用于向指定元素添加事件句柄
    
        e.preventDefault();
        // 取消该事件

        console.log("click",e.target.innerHTML);
        // target 事件属性返回触发事件的元素。

        GM_setClipboard(e.target.innerHTML);
        //复制 文本 到剪贴板
        
    
    })

}) ();
