// ==UserScript==
// @name         mydigit.cn_sign
// @namespace    https://www.mydigit.cn/
// @version      0.1.0
// @description  数码之家-论坛，(家电，u盘的论坛)-定时签到脚本，每日1次，需要先登陆
// @author       zip11
// @grant       GM_xmlhttpRequest
// @grant       GM_notification
// @grant       GM_log
// @connect     www.mydigit.cn
// @crontab      2-59 * once * *
// ==/UserScript==



'use strict';

function hash(wz1) {

    // bbs 获取 mhash
    
    return new Promise((resolve, reject) => {
            

        GM_xmlhttpRequest({

            method: "get",
            url: wz1,
            headers: {
                "upgrade-insecure-requests": "1" ,
                //用于让浏览器自动升级请求从http到https,用于大量包含http资源的http 
                'Referer':wz1          
            },

            onload: function(xhr){
                
                console.log("mhash-请求成功");

                let nr = xhr.responseText
                //响应 文本

                console.log(nr);

                // 提取 网页的mhash -start

                let parser = new DOMParser();
                let doc = parser.parseFromString(nr, "text/html")
                // string类型的 html文本转换成 dom结构

                let formhash = doc.querySelector(`input[name="formhash"]`).value;
                // css 选择器

                console.log(formhash)
                //GM_notification(formhash)

                resolve(formhash);
        
            },

            onerror: function(response){

            //console.log("请求失败");
                reject("mhash请求失败"+response);
            }
        });
        


        /*

        
    */

    });

}

function bbs_sign(wz2,hash1) {
    
    // bbs 签到 post

    if (typeof hash1 == 'string' && hash1.length > 0) {

        //判断字符串不为 空

        

        return new Promise((resolve, reject) => {

            // get 签到-网址+ mhash
            wz2 =wz2 + hash1

            GM_xmlhttpRequest({
                
                method: "GET",
                url: wz2,
                headers: {
                    "x-requested-with": "XMLHttpRequest",
                    'Referer':'https://www.mydigit.cn/k_misign-sign.html'
    
                },
    
                
    
                // 签到 执行 完成
                onload: function(xhr){

                    console.log("SIGN-请求成功");
                    console.log(xhr.responseText);
                    
                    let text = "";

                    if (xhr.responseText.includes("CDATA[]]")) {
                        
                        text = "bbs定时签到成功"
                        //GM_notification(text)
                        resolve(text)
    
                    } else if (xhr.responseText.includes("今日已签")) {
                        
                        text = "bbs定时签到失败 - 重复签到"
                        //GM_notification(text)
                        resolve(text)
    
                    } else {
                        
                        text = "bbs定时签到失败-未知错误-详见调试-mhash:" + hash1 
                        //GM_notification(text)
                        reject(text)
                    }
            
                    // resolve(xhr.responseText);
            
                },
    
                // 签到 错误
                onerror: function(response){

                    console.log("SIGN-请求失败"+response);
                    reject("请求失败");
                
                }

            });
        });
    }

    else {
        return "mhash为空无法签到"
    }



}


async function run1() {


    const hh = await hash("https://www.mydigit.cn/k_misign-sign.html");

    GM_notification({
        text:hh,
        timeout: 2000
    });
    // mhash 获取

    let sign_wz = "https://www.mydigit.cn/plugin.php?id=k_misign:sign&operation=qiandao&format=empty&inajax=1&ajaxtarget=&formhash="
    const sign_msg = await bbs_sign(sign_wz,hh);


    GM_notification({
        text:sign_msg,
        timeout: 2000
    });

    // bbs 签到 get

    if(sign_msg!=="bbs定时签到成功") {
        // 错误-日志保存

        //GM_log(sign_msg,"error");
        return(sign_msg);                
        
    } else {

        //签到 成功
        GM_log(sign_msg,"info");
        return(sign_msg);  
        
    }

}



return new Promise(async (resolve, reject) => {

    try {

        let jg8 = await run1();

        if (jg8 == "bbs定时签到成功") {
        
            resolve("ok"+jg8);
            // 执行成功
        
        } else {
        
            reject("error-exit"+jg8);
            // 执行失败,并返回错误原因
        
        }        

    } catch (error) {

        //GM_log(error);
        reject(error);
    }

});

