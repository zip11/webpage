## then()方法 ##

then()方法是异步执行。

意思是：就是当.then()前的方法执行完后再执行then()内部的程序，这样就避免了，数据没获取到等的问题。

语法：promise.then(onCompleted, onRejected);

**参数**

promise
必需。
Promise 对象。

onCompleted
必需。
承诺成功完成时要运行的履行处理程序函数。

onRejected
可选。
承诺被拒绝时要运行的错误处理程序函数。


----------

[https://blog.csdn.net/maxiaoyin111111/article/details/84842292](https://blog.csdn.net/maxiaoyin111111/article/details/84842292)

### ES6中允许使用“箭头”(=>)定义函数 ###

    var f   = v => v;
    
    
    var function(v){
    	return v;
    }

**无参数的箭头函数**

    var f = ()=>5;
    
    
    var function(){
    	return 5;
    }