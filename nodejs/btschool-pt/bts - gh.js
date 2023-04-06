//  cjm old version ,npm install node-fetch@2.6.2 -save
const fetch = require('node-fetch')

// request  no esm;
const request = require('request');

var cookie1,wh;

cookie1="";
// wchat webhook
wh="";




fetch("https://pt.btschool.club/index.php?action=addbonus", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "cookie": cookie1,
    "Referer": "https://pt.btschool.club/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": null,
  "method": "GET"
})
    .then(res=>res.text())
    // .then(res=>console.log(res))
    .then(function (res) {

        if(res.indexOf("今天签到您获得") != -1){

          console.log("bts-pt sign ok");
          retd("btschool-pt-sign-ok");

        } else {

            // pt-sign-error,wx-send-msg
            retd("btschool-pt-sign-error") ;
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

function retd(xxts) {

  // send wx msg ,sign error ,day-7

  // day is ?
  var date=new Date(); 
  var day=date.getDay();

  if(day==0){

    resData.text.content=xxts;
    requestfun();
  }
  return day

}