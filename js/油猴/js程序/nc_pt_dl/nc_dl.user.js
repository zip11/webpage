// ==UserScript==
// @name         nc_pt_下载文件
// @namespace    nc-dl
// @version      0.1.0
// @description  批量-下载文件
// @author       2024-02-26
// @match        https://www.nicept.net/torrents.php?inclbookmarked=1&allsec=1&incldead=0
// @match        https://www.pttime.org/bookmarks.php?inclbookmarked=1&incldead=0
// @grant        GM_notification
// ==/UserScript==

(function() {

    var button = document.createElement('button');
    
    button.innerHTML = '批量下载';
    button.style.position = 'fixed';
    // 按钮 垂直 位置
    button.style.bottom = '10px';
    // 按钮与 左侧距离
    button.style.left = '10px';
    // 按钮 堆叠 顺序，越大，越在顶层
    button.style.zIndex = '1000';
    
    // 添加 按钮
    document.body.appendChild(button);

    // 按钮 点击
    button.addEventListener('click', function() {
        
        // 批量 下载 文件
        dl_tor();
    });

})();

// 下载 文件
async function dl_tor() {


    //开始 结束 网址

    let st_wz = window.prompt("输入-开始-下载链接-网址");
    let end_wz = window.prompt("输入-结束-下载链接-网址");

    // 输入 空 ，错误，退出
    if (st_wz === null || end_wz === null) {
        
        const cw = "input null,error";
        console.log(cw)
        msgbox9(cw);
        return "error"
    }

    // 开始 结束 ，数组 序号
    var st_num = -1;
    var end_num = -1;


    // 获取所有-下载链接

    let wz4 = document.querySelectorAll('a[href^="download.php?id"]');


    // 搜索 数组 序号，st~~~~~~~~~~~~
    for (let i = 0; i < wz4.length; i++) {

        // 当前 网址
        let dwz = wz4[i].href;
        // console.log("dl-wz: " + dwz);
        
        // 开始 序号，判断
        if(dwz === st_wz) {
            st_num = i ;
        }

        // 开始序号 搜索完成，结束位置 匹配 找到
        if(st_num !== -1 && dwz === end_wz){
            end_num = i + 1 ;
        }

    }

    // 网址搜索 失败，退出 函数
    if (st_num === -1 || end_num === -1) {

        msgbox9("网址搜索失败")
        return "error,no find"
    }

    // end ~~~~~~~~~~

    // 对象 转 数组
    let wz5 = Array.from(wz4);

    // 截取 数组
    let jq_wz = wz5.slice(st_num,end_num);

    console.log("获取搜索链接:",jq_wz)
    msgbox9("下载文件数量:" + jq_wz.length);

    // 下载 文件
    for (let item of jq_wz) {

        console.log("下载文件-start:",item);
        
        // 等待 3s
        await sleep1(3);
        
        // 打开 新窗口
        window.open(item);
        
    }

    // 下载完成 
    const wc = "下载文件-完成-数量: " + jq_wz.length  + "！！！"
    msgbox9(wc);
    console.log(wc);

    // 删除书签
    bookmark_del(st_num,end_num);


}

function bookmark_del(st_num1,end_num1) {

    // 删除书签 st~~~~~~~~~~~

    // 获取所有 书签，转数组
    // 点击 指定 a 链接

    msgbox9("取消 下载 书签-开始");
    // 获取所有 书签
    let bk_all = document.querySelectorAll('a[id^="bookmark"]')
    // 正则表达式通常使用 RegExp 对象来表示。这段代码中，^ 符号表示字符串的开始

    // 对象 转 数组
    let bk_sz = Array.from(bk_all);

    // 遍历 删除 书签
    for(let i = st_num1 ; i < end_num1; i++) {
        
        // 取消 收藏
        bk_sz[i].click();
    }

    console.log("书签 删除 完成");
    // end ~~~~~~~~~~~~
}

// 异步 延时
function sleep1(time) {

    time*=1000
    return new Promise(resolve => {

        setTimeout(() => {
            resolve();
        }, time);
    });
}

// 消息框
function msgbox9(msg) {

    GM_notification({

        title: msg,
        text: msg,
        timeout: 2000,
        highlight: false,
    
    })

}
