   //引入需要的模块

    // node-schedule 为定时任务模块  
    // const schedule = require("node-schedule");

    // request 为请求第三方接口模块
    const request = require('request');
   
  // resData对象各属性请参考官方文档
  // https://developer.work.weixin.qq.com/document/path/91770

    // js object key:value
    var resData = {
        "msgtype": "text",
        "text": {
            "content": "需要发送的消息",
            "mentioned_list": ["@all"],
            "mentioned_mobile_list":[""]
        }
    };

    function requestfun() {

          // url 为企业机器人的webhook
         request({
            url: "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a111",
            method: "POST",
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify(resData)
            // .stringify 方法将 JavaScript 对象转换为字符串
        }, function (error, response, body) {
            console.log('提示成功！');
        });
    }

    // const scheduleCronstyle = () => {
    //     //每分钟的第30秒定时执行一次:
    //     schedule.scheduleJob('0 15 18 * * 1-5', () => {
    //         requestfun();
    //         // console.log('scheduleCronstyle:' + new Date());
    //     });
    // }

    // scheduleCronstyle();

    // resdata type
    console.log("type resdata:"+typeof(resData) );

    // send msg text value
    resData.text.content="test123"
    console.log("resdata text:"+resData.text.content);

    // send msg
    requestfun();
    console.log('Start successfully');