

var fun =function(){

    var exec = require('child_process').execFile;

    console.log("fun() start");

    exec('ping',["www.baidu.com"], function(err, data) {  

        if (err === null) 
            console.log(data.toString());  
        else
            console.log(err);    
          

    });  

}

fun();