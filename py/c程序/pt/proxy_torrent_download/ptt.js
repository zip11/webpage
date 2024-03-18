// ==UserScript==
// @name         proxy_download_torrent
// @namespace    https://bbs.tampermonkey.net.cn/
// @version      0.1.0
// @description  代理下载种子
// @author       09-25-2023
// @match        https://www.pttime.org/details.php?id=*
// ==/UserScript==

(function() {
    'use strict';

    //~~~~~~~~~~Add  button3 ~~~~~~~~~~~


    let mybtn = document.createElement('button');
	
	// 添加 body 按钮，浮动
    document.body.appendChild(mybtn);

    mybtn.id = 'my-btn';
    mybtn.innerHTML = `代理下载种子
<style>
#my-btn {
    /* position设置为fixed，固定位置，即使窗口滚动位置不变 */
    position: fixed;
    top: 100px;
    left: 30px;
    width: 150px;
}
</style>`

// 获取下载网址
let wztor = document.querySelector("#download_url");

console.log(wztor.value);

// 下载文件 标题
let file_title = document.querySelector("#top").textContent

// 下载软件网址
let proxy_web = "http://127.0.0.1:5000/api/get?name=";

var proxy_url =  ""

// get 网址
proxy_url = proxy_web + encodeURIComponent(wztor.value) + "&title=" + file_title

console.log(proxy_url);

    // 按钮点击
    mybtn.onclick = function () {
	
	//  开始 下载
    window.location.href = proxy_url
	}
})();