## Node.js发送请求 ##
Node.js发送请求，需要用到request这个模块
request官网
先导入这个模块

    npm install request --save

GET请求

    var url = 'http://192.168.0.102:3000/home?name=xmg'
    
    // 发送Get请求
    // 第一个参数:请求的完整URL,包括参数
    // 第二个参数:请求结果回调函数,会传入3个参数,第一个错误,第二个响应对象,第三个请求数据
    request(url,function (error, response, data) {
       
    	console.log(data)
    
    });

## Post请求 ##
post请求有3种方式，由请求头中的content-type决定，属于哪一种post请求
application/x-www-form-urlencoded： 普通http请求方式，参数是普通的url参数拼接
application/json： JSON请求方式，参数是json格式
multipart/form-data: 文件上传
application/x-www-form-urlencoded
    var url = 'http://192.168.0.102:3000/home?name=xmg'
    
    request.post({url:url, form:{key:'value'}}, function(error, response, body) {
	    if (!error && response.statusCode == 200) {
	    }
    })
### application/json ###
    var url = 'http://192.168.0.102:3000/home'
    
    request({
	    url: url,
	    method: "POST",
	    json: true,
	    headers: {
	    	"content-type": "application/json",
	    },
	    body: JSON.stringify(requestData)
	   }, function(error, response, body) {
	    if (!error && response.statusCode == 200) {
	    }
    }); 

multipart/form-data


    var url = 'http://192.168.0.102:3000/home'
    var formData = {
	    // Pass a simple key-value pair
	    my_field: 'my_value',
	    // Pass data via Buffers
	    my_buffer: new Buffer([1, 2, 3]),
	    // Pass data via Streams
	    my_file: fs.createReadStream(__dirname + '/unicycle.jpg'),
    };
    request.post({url:url, formData: formData}, function (error, response, body) {  
	    if (!error && response.statusCode == 200) {
	    }
    })

作者：袁峥
链接：https://www.jianshu.com/p/a156729ce499
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。