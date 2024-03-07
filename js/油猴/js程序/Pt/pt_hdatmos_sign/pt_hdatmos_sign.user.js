// ==UserScript==
// @name         pt_hdatmos_nictpt_sign
// @namespace    pt_hdatmos_sign2
// @version      0.1.0
// @description  hdatmos ,nicept ,sign
// @author       24-3-6
// @crontab      * * once * *
// @grant        GM_xmlhttpRequest
// @connect     hdatmos.club
// @connect     www.nicept.net
// @grant        GM_notification
// ==/UserScript==

// 签到 函数，网址，网站名字
function sign(url,website_name) {

    return new Promise((resolve, reject) => {

        // 定义目标URL
        let targetUrl = url; 
        

        // 发送GET请求
        GM_xmlhttpRequest({

            method: 'GET',
            url: targetUrl,
            
            onload: function(response) {

                // 请求成功，显示返回的内容
                // console.log(website_name + ' 返回的内容：');

                // 网页 返回 文本
                let webtext = response.responseText;
                

                // 判断 成功 字符串
                if(webtext.indexOf('到已得') != -1) {
                    
                    GM_notification(website_name + ' 签到 完成');
                    resolve( website_name + "_sign ok");

                } else {

                    // 签到错误 
                    console.log(website_name + "~~~~~~~~~" +webtext);
                    GM_notification(website_name + ' 签到 失败');
                    reject(website_name + "_sign fail");
                }

            },
            onerror: function(error) {

                // 请求失败，显示错误信息
                console.error(website_name + ' 请求失败：', error);
                
                // 弹出提示框
                GM_notification(website_name + ' 请求失败：', error);

                reject(website_name + "_sign error"); 
                // 执行失败,并返回错误原因
            }

        }); 

    });

}

// 定时 脚本
return new Promise((resolve, reject) => {

    'use strict';

    // hdatoms
    sign('https://hdatmos.club/attendance.php', 'hdatmos');
    
    // nicept
    sign('https://www.nicept.net/attendance.php', 'nicept');

});