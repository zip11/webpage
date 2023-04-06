//  cjm old version ,npm install node-fetch@2.6.2 -save
const fetch = require('node-fetch')
//  import fetch from "node-fetch";

// jsdom
const jsdom = require("jsdom");
const jquery = require('jquery');



// 获取签到网页-源代码

async function hash1(cookie4) {


    
  const res = await fetch(qdwz, {
      "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": cookie4
      },
      "body": null,
      "method": "GET"
    });

  const result = await res.text();

  return result;

}

// 获取bbs mhash

function mhh1(nr1) {


  // 获取html dom元素 文本， jsdom是html dom 解析器

  const { JSDOM } = jsdom;

  var dom = new JSDOM(nr1);;


  var window = dom.window; 
  // 获取 window 对象

  var document = dom.window.document; 
  // 获取 document 对象

  var $ = jquery(window); 
  // 实例化jquery需要传入window对象

  // body ----s
  //console.log(document.body.innerHTML);
  // body html
  //console.log($("body").html());

  // input 获取 value
  let mhh = $("input[name=\"formhash\"]").val()
  console.log("mhash:"+mhh);

  return mhh;

}

module.exports = {
  hash1,
  mhh1
}




   