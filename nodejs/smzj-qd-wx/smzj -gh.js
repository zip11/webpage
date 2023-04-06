//  cjm old version ,npm install node-fetch@2.6.2 -save
const fetch = require('node-fetch')
//  import fetch from "node-fetch";

// request  no esm;
const request = require('request');

var hh1 = require('./smzj_mhash') 

var cookie3,wh;

cookie3="";
// smzj cookie
wh="";
// weixin webhook

qdwz = "https://www.mydigit.cn/k_misign-sign.html";


    


// 检查是否 已经 签到
async function qdhash() {

  const result1 =  await hh1.hash1(cookie3);
  // 获取mhash 网页源码 文本

  // 显示 签到网页 内容
  // console.log(result1);

  // 检查 是否 已经签到
  if(result1.indexOf("您的签到排名") != -1){

    console.log("smzj sign ok,exit");

    // let mhhcode = hh1.mhh1(result1);
    // jsdom 获取 mhash

  } else {

    console.log("smzj sign no,ajax-sign-start");

    let mhhcode = hh1.mhh1(result1);
    
    // jsdom 获取 mhash

    qdajax(cookie3,mhhcode);
    //  ajax 签到
  }

} 




//  签到按钮 post
function qdajax(cookie3,mhh) {

  fetch("https://www.mydigit.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash="+mhh+"&format=empty&inajax=1&ajaxtarget=", {
    "headers": {
      "accept": "*/*",
      "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
      "sec-ch-ua": "\"Microsoft Edge\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "\"Windows\"",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-requested-with": "XMLHttpRequest",
      "cookie": cookie3,
      "Referer": qdwz,
      "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": null,
    "method": "GET"
  })
      .then(res=>res.text())
      
      .then(function (res) {


          // console.log(res);
          // 网页内容

          if(res.indexOf("CDATA[]]") != -1){
      
            console.log("smzj sign ok-ajax");
  
            // day-7 wx-msg-send
            retd();
  
            
          } else if(res.indexOf("今日已签") != -1){
              
            console.log("smzj-today signed");
            
            // send msg text value
            resData.text.content="smzj-today signed"
             // day-7 wx-msg-send
             retd();
              
          } else {
  
            console.log("smzj sign error");
            resData.text.content="smzj-sign-error"
            requestfun();
            
          }
        
        
      });
}


   
  //resData对象各属性请参考官方文档
  // https://work.weixin.qq.com/help?doc_id=13376
    var resData = {
        "msgtype": "text",
        "text": {
            "content": "smzj-sign-msg-text",
            "mentioned_list": ["@all"],
            "mentioned_mobile_list":[""]
        }
    };

    function requestfun() {
          // url 为企业机器人的webhook
         request({
            url: "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="+wh,
            method: "POST",
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify(resData)
        }, function (error, response, body) {
            console.log('提示成功！');
        });
    }

function retd() {
  
  // send wx msg ,sign ok ,day-7

    // day is ?
    var date=new Date(); 
    var day=date.getDay();

    if(day==0){

      resData.text.content="smzj-sign-ok-day7";
      requestfun();
    }
    return day


}



//  开始签到
qdhash();