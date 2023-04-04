// ==UserScript==
// @name         文本插入
// @namespace    https://bbs.tampermonkey.net.cn/
// @version      0.1.0
// @description  文本插入
// @author       You
// @match        https://bbs.tampermonkey.net.cn/ 
// @grant GM_notification

// ==/UserScript==

(function() {

    let div=document.createElement("div");

    div.innerHTML='<span id="span-1">span1</span><span class="sp">span class</span>';

    div.onclick=function(event){

        if(event.target.id=="span-1"){
            alert("span-1被点击了");
        
        }else if(event.target.className=="sp"){
            alert("sp这一类被点了");
        }
    };

    //document.body.append(div);
    //document.body.insertBefore(div,document.body.children[0]);
    let dest = document.querySelector(".z");

    dest.append(div);

})();