[https://bbs.tampermonkey.net.cn/thread-237-1-1.html](https://bbs.tampermonkey.net.cn/thread-237-1-1.html)

## 脚本往页面添加新元素 ##

脚本往页面增加新元素这种需求经常可见,例如百度云的脚本,就会往页面上添加一些解析链接之类的按钮,一些助手类型的会往页面上添加一些小窗口,显示脚本的运行状态等等.

如果要让脚本往页面上添加新元素,原理很简单.

首先使用 document.createElement创建好你想插入的元素,例如按钮就 document.createElement("button"),如果你有很多组件想放进去的话可以用 document.createElement("div"),然后往element里的innerHTML直接写html代码.

然后找到你想插入的位置,使用 append/insertBefore之类的方法插入你的element.之后就可以在 F12 开发者工具中的 element中看到我们插入的内容了.


## 新元素的事件监听 ##

> 元素是添加进去了,但是只能看又不能用那有啥用.所以我们需要监听我们的元素事件,最常用的就是 click点击事件,点了我们的按钮,让我们的脚本做出一些反应.

如果是类似按钮的方式,我们可以这样写.直接的使用onclick的方法.


    let btn=document.createElement("button");

    btn.innerHTML="按钮文字,其实也可以写html,变成下面的样子(不过谁用按钮来包那么多html标签呢)";
    //innerText也可以,区别是innerText不会解析html
    
    btn.onclick=function(){
    //code
        alert("点击了按钮");
    }

    document.body.append(btn);

如果是一个div,在里面写html自由发挥,可以使用下面的方式.event详细说明:Event

    let div=document.createElement("div");

    div.innerHTML='<span id="span-1">span1</span><span class="sp">span class</span>';

    div.onclick=function(event){

	    if(event.target.id=="span-1"){
	    	alert("span-1被点击了");
	    }else if(event.target.className=="sp"){
	    	alert("sp这一类被点了");
	    }
    };
    document.body.append(div);


至于为什么会有这样的区别,简单来说就是前一种方法我们监听的只有一个元素,那我们肯定就知道就只可能是这一个执行的操作.

后面的因为里面包含了多个元素,我们就可以从event里面找到实际被点击的元素,通过id或者class去判断,来走我们的脚本执行流程.

另外再补充一下,上面的onclick可以改写成addEventListener("click"),类似下面这样.

    div.addEventListener("click",function(ev){
    	console.log(ev);
    });

主要区别onclick只能绑定一个function,addEventListener可以绑定多个,这又涉及了前端的内容,大家可以课后补习一下,可以看一下addEventListener的说明.也还有其它的绑定事件的方法,这里就不一一列举了.

对于监听页面上已经有的按钮,推荐用addEventListener,以防onclick将原来的按钮事件覆盖掉(如果按钮也是用onclick的话),看情况而定.

而且也可以在事件中 return false;使事件不再向上传递.

## 新元素的style ##

为了好看或者放在网页中不突兀,我们可以加上网页自带的class或者自己写一些样式,类似下面这样:

    btn.className="default-btn";
	//添加class
    
	btn.id="submit-btn";
	//添加id
    
	btn.style.color="#ff0000";
	//给按钮写style样式,查看这个文档,看css与JavaScript的对应:https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference
    
	div.innerHTML='<span id="span-1" class="span-class" style="font-size:12px">span1</span><span class="sp" style="color:red">span class</span>';
	//在html里写style