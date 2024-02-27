// ==UserScript==
// @name         数码之家签到
// @namespace    mydigit_sign
// @version      1.0
// @description  数码之家论坛签到，论坛账户提前登录(登录设置保存登录状态)，打开游览器后，使用脚本猫每天定时启动签到
// @author       zip11
// @grant        GM_xmlhttpRequest
// @grant        GM_notification
// @crontab      1-59 * once * *
// @connect     www.mydigit.cn
// ==/UserScript==


'use strict';


// 读取 按钮 签到链接
function read_button_link() {

    // 使用GM_xmlhttpRequest获取页面内容，并提取id为JD_sign的<a>标签的href属性
    // 替换为你想要请求的URL
    var targetUrl = 'https://www.mydigit.cn/k_misign-sign.html';

    // 读取 签到按钮 链接
    GM_xmlhttpRequest({

        method: 'GET',
        url: targetUrl,
        onload: function(response) {

            // 解析响应内容
            var doc = new DOMParser().parseFromString(response.responseText, 'text/html');
            
            // 按钮 id
            var link = doc.querySelector('#JD_sign');
            
            // 网址 非空
            if (link && link.href) {
            
                // 如果找到了链接，将其保存到GM_setValue中，以便在页面上显示或使用
                // GM_setValue('JD_sign_href', link.href);

                // 在控制台输出或在页面上显示链接
                console.log('找到链接：', link.href);

                // 访问 签到网址
                sign_page(link.href);

                resolve("read_link_ok")

            } else {

                // 获取 签到链接 失败
                console.log('未找到ID为JD_sign的链接');
                msgk('未找到ID为JD_sign的链接')
                reject("read_link_error")
            }
        },
        onerror: function(error) {
            console.error('请求失败：', error);
        }
    });   
}

// 访问 签到网址
function sign_page(link2) {

    // 如果找到了链接，使用GM_xmlhttpRequest再次发送GET请求
    GM_xmlhttpRequest({

        method: 'GET',
        url: link2,
        onload: function(getResponse) {

            // 显示返回的内容
            console.log('返回的内容：');
            console.log(getResponse.responseText);

            // 签到 成功 检测
            let pageContent = getResponse.responseText;
            // 签到 成功 字符串
            let targetString = "CDATA[]";

            // 使用indexOf检查字符串是否存在
            if (pageContent.indexOf(targetString) > -1) {
                console.log('签到成功：存在', targetString);
                msgk('签到成功：存在' + targetString)
                return "ok"
            } else {
                console.log('签到出错：不存在', targetString);
                msgk('签到出错：不存在' + targetString)
                return "error"
                
            }

        },
        onerror: function(error) {
            console.error('请求失败：', error);
        }
    });        

}



// 消息框，自动关闭 函数
function msgk(text,sec) {

    // sec 如果没有输入参数，sec = 3
    if (!sec) sec = 3;

    GM_notification({
        title: "Auto Close Notification",
        text: text,
        silent: true, // 是否在通知栏显示
        timeout: sec*1000 // X秒后自动关闭
    });

}



// main 主函数
return new Promise((resolve, reject) => {
    
    try {

        // 读取按钮链接
        let button_msg = read_button_link();

        // 判断 签到链接 获取成功
        if(button_msg == "read_link_ok") {
            
            resolve("read-sign-link-ok");
            // 执行成功
        } else {
            reject("read-sign-link-error");
        }

        

    } catch (error) {

        //GM_log(error);
        reject(error);
    }
});