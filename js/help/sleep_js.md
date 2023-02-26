
[https://www.runoob.com/js/js-async.html](https://www.runoob.com/js/js-async.html)

## 同步执行延迟 ##

阻塞其他油猴脚本和网页加载, 

    function syncSleep(time) {
      const start = new Date().getTime();
      while (new Date().getTime() - start < time) {}
    }

---

## 异步延迟 ##

	// ==UserScript==
	// @name 测试油猴4
	// @namespacehttp://tampermonkey.net/
	// @version  0.1
	// @description  try to take over the world!
	// @author   You
	// @match*://*/*
	// @icon https://www.google.com/s2/favicons?sz=64&domain=baidu.com
	// @grantnone
	// ==/UserScript==
	
	function log(msg){
	console.log(msg)
	}
	
		 function sleep1(time) {
			time*=1000
			return new Promise(resolve => {
			setTimeout(() => {
			resolve();
			}, time);
			});
		}
	
	// 油猴主函数,加上async 改成异步函数; 在内部使用await sleep()来调用异步延迟

	(async function() {
		'use strict';
		
		// Your code here...
		
		log(`异步测试油猴1`)
		await sleep1(3)
		document.querySelector("a.c-font-normal.c-color-gray2.hot-refresh").click()
		log(`异步测试油猴2`)
		await sleep1(3)
		document.querySelector("a.c-font-normal.c-color-gray2.hot-refresh").click()
	
	})();