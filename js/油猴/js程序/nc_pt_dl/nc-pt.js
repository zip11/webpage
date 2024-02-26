
/*
let wz_all;


wz_all = ""
for (let item of wz4) {
    console.log(item.href);
    wz_all = wz_all + item.href + ';';
}

console.log(wz_all);
*/

// 获取 下载链接 文件

// 获取所有-下载链接

let wz4 = document.querySelectorAll('a[href^="download.php?id"]');


//开始 结束 网址

let st_wz = "";
let end_wz = "";

// 开始 结束 ，数组 序号
var st_num = -1;
var end_num = -1;


// 搜索 数组 序号，st~~~~~~~~~~~~
for (var i = 0; i < wz4.length; i++) {

    // 当前 网址
    let dwz = wz4[i].href;
    console.log(dwz);
    
    // 开始 序号，判断
    if(dwz === st_wz) {
        st_num = i ;
    }

    // 开始序号 搜索完成，结束位置 匹配 找到
    if(st_num !== -1 && dwz === end_wz){
        end_num = i + 1 ;
    }

}
// end ~~~~~~~~~~

// 对象 转 数组
let wz5 = Array.from(wz4);

// 截取 数组
let jq_wz = wz5.slice(st_num,end_num);

console.log("获取搜索链接:",jq_wz)

// 下载 文件
for (let item of jq_wz) {

    console.log("dl-tor",item);
    
    // 等待 3s
    setTimeout(window.open(item), 3000);
}

// 删除书签

// 获取所有 书签，转数组
// 点击 指定 a 链接

// 获取所有 书签
let bk_all = document.querySelectorAll('a[id^="bookmark"]')
// 正则表达式通常使用 RegExp 对象来表示。这段代码中，^ 符号表示字符串的开始

// 对象 转 数组
let bk_sz = Array.from(bk_all);

// 遍历 删除 书签
for(let i = st_num ; i < end_num; i++) {
    
    // 取消 收藏
    bk_sz[i].click();
}