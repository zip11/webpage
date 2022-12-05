// smzj discuz sigh,cookie and formhash(5 month)
import fetch from "node-fetch";
fetch("https://www.mydigit.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash=123abcdef&format=empty&inajax=1&ajaxtarget=", {
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
    "cookie": "",
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
        
      } else if(res.indexOf("今日已签") != -1){
          
        console.log("today signed");
          
      } else {

        console.log("smzj sign error");
      }
  
  
});