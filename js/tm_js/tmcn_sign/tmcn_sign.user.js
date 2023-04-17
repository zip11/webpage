// ==UserScript==
// @name         油猴中文网_sign
// @namespace    https://bbs.tampermonkey.net.cn/
// @version      0.1.0
// @description  油猴中文网论坛-定时签到脚本，每日1次，需要先登陆
// @author       zip11
// @grant       GM_xmlhttpRequest
// @grant       GM_notification
// @grant       GM_log
// @connect     bbs.tampermonkey.net.cn
// @crontab      1-59 * once * *
// ==/UserScript==



'use strict';



function hash(wz1) {

    // bbs 获取 mhash

    return new Promise((resolve, reject) => {


        GM_xmlhttpRequest({

            method: "get",
            url: wz1,
            headers: {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            },

            onload: function (xhr) {

                console.log("请求成功");

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

            onerror: function (response) {

                //console.log("请求失败");
                reject("请求失败" + response);
            }
        });


    });

}

function tmcn_sign(hash1) {

    // bbs 签到 post

    return new Promise((resolve, reject) => {

        if (typeof hash1 == 'string' && hash1.length > 0) {
        //判断字符串不为 空

            let body1 = "formhash=" + hash1 + "&qdxq=fd&qdmode=3&todaysay=&fastreply=0"

            GM_xmlhttpRequest({

                method: "POST",
                url: "https://bbs.tampermonkey.net.cn/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
                    'Referer':'https://bbs.tampermonkey.net.cn/dsu_paulsign-sign.html'

                },

                data: body1,

                // 签到 执行 完成
                onload: function (xhr) {

                    let text = '';

                    console.log("请求成功");
                    //console.log(xhr.responseText);

                    if (xhr.responseText.includes("签到成功")) {

                        text = "油猴中文网bbs定时签到成功"
                        //GM_notification(text)
                        resolve(text)

                    } else if (xhr.responseText.includes("已经签到")) {

                        text = "油猴中文网bbs定时签到失败 - 重复签到"
                        //GM_notification(text)
                        resolve(text)

                    } else {

                        text = "油猴中文网bbs定时签到失败-未知错误-详见调试-mhash:" + hash1 + "\nbody1:" + body1
                        //GM_notification(text)
                        reject(text)
                    }

                    // resolve(xhr.responseText);

                },

                // 签到 错误
                onerror: function (response) {

                    console.log("请求失败" + response);
                    reject("bbs请求失败" + response);

                }

            });
        

        } else {
            reject("mhash为空无法签到");
            //return 
        }

    });

}

// 异步 延时 秒
function sleep1(time) {

    time*=1000
    return new Promise(resolve => {
        setTimeout(() => {
            resolve();
        }, time);
    });
}

//  随机数
function sj_num() {

    //Math.random() 产生 0-1
    // floor 取整数 向下

    let sjs = Math.floor(Math.random() * (6-2) );
    
    sjs = sjs + 2
    
    // 可均衡获取 2 到 6 的随机整数。
    
    return sjs;

}

// 开始 签到bbs
async function run1() {

    const hh = await hash("https://bbs.tampermonkey.net.cn/thread-184-1-1.html");
    //GM_notification(hh);
    // mhash 获取


    let sjnum = sj_num();
    //随机 延时 2-6 min
    await sleep1(sjnum*60);

    const sign_msg = await tmcn_sign(hh);
    GM_notification(sign_msg);

    if(sign_msg!=="油猴中文网bbs定时签到成功") {

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

        if (jg8 == "油猴中文网bbs定时签到成功") {
        
            resolve("ok"+jg8);// 执行成功
        
        } else {
        
            reject("error-exit"+jg8);// 执行失败,并返回错误原因
        
        }        

    } catch (error) {

        //GM_log(error);
        reject(error);
    }

});

