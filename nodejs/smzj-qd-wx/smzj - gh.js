//  cjm old version ,npm install node-fetch@2.6.2 -save
const fetch = require('node-fetch')
//  import fetch from "node-fetch";

// request  no esm;
const request = require('request');


var mhh,cookie1,wh;

mhh="";
cookie1="";
wh="";

  

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
    "cookie": cookie1,
    "Referer": "https://www.mydigit.cn/k_misign-sign.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
})
    .then(res=>res.text())
    // .then(res=>console.log(res))
    .then(function (res) {
      
        if(res.indexOf("CDATA[]]") != -1){
    
          console.log("smzj sign ok");

          // day-7 wx-msg-send
          retd();

          
        } else if(res.indexOf("今日已签") != -1){
            
          console.log("smzj-today signed");
          
          // send msg text value
          resData.text.content="smzj-today signed"
          requestfun();
            
        } else {

          console.log("smzj sign error");
          resData.text.content="smzj-sign-error"
          requestfun();
          
        }
      
      
    });


   
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



    
