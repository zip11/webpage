// ==UserScript==
// @name         pt-title-copy
// @namespace    pt-Script Scripts
// @version      0.1
// @description  pt web :mt-ptt  title video number copy clip
// @author       clip
// @match        https://kp.m-team.cc/details.php*
// @match        https://www.pttime.org/details.php*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        GM_setClipboard
// ==/UserScript==

(function () {
	'use strict';
	console.log('脚本加载pt-title-copy');

     //创建复制视频番号（按钮）
	var button = document.createElement("button");

    //按钮 属性
	button.id = "id001";
	button.textContent = "复制视频番号";
	button.style.width = "120px";
	button.style.height = "20px";
	button.style.align = "center";
    //~~~~~~~~~end~~~~~~~


     //创建一个复制中文标题（按钮）
	var button2 = document.createElement("button");

    //复制视频番号 ,按钮 属性
	button2.id = "id002";
	button2.textContent = "复制中文标题";
	button2.style.width = "90px";
	button2.style.height = "20px";
	button2.style.align = "center";
    //~~~~~~~~~end~~~~~~~


    //创建一个复制dmm 图片网址（按钮）
	var button3 = document.createElement("button");

    //复制视频番号 ,按钮 属性
	button3.id = "id003";
	button3.textContent = "复制dmm-img";
	button3.style.width = "120px";
	button3.style.height = "20px";
	button3.style.align = "center";
    //~~~~~~~~~end~~~~~~~

    //创建 复制 海报封面 图片网址（按钮）
	var button4 = document.createElement("button");

    //复制视频番号 ,按钮 属性
	button4.id = "id004";
	button4.textContent = "复制封面图片";
	button4.style.width = "120px";
	button4.style.height = "20px";
	button4.style.align = "center";



    //~~~~~~Button onclick ~~~~~~~~~~~



	//复制视频番号  , 绑定按键点击功能
	button.onclick = function (){

		console.log('点击了按键');

        //获取标题 文本
        var bt1 = document.querySelector('h1');
        var btnr = bt1.innerText

        //删除中文
        var btnr1 = RemoveChinese(btnr);

        //复制 剪贴板
        GM_setClipboard(btnr1);

        //修改标题
        bt1.textContent = btnr1
		//alert(btnr1);

        return;
	};
    //~~~~~~~~~end~~~~~~~



	// 复制中文 标题 按钮 ，绑定按键点击功能
	button2.onclick = function (){

		console.log('点击了按键,复制中文');

        //获取标题 文本
        var bt1 = document.querySelector('.rowfollow[valign="top"]');
        var btnr = bt1.innerText

        //
        var btnr1 = btnr;

        //复制 剪贴板
        GM_setClipboard(btnr1);

        //修改标题
        bt1.textContent = btnr1
		//alert(btnr1);

        return;
	};
    //~~~~~~~~~end~~~~~~~







	// 复制dmm img 按钮 ，绑定按键点击功能
	button3.onclick = function (){

        picsnap()

        
	};

    function picsnap() {

        // 多个视频 大图
        
        console.log('点击了按键,复制dmm img');

        var dmmimg=document.querySelectorAll('.dmm_pic>img')

        var i;
        //bbcode img
        var dmmwz='';
        
        for (i = 0; i < dmmimg.length; i++) {

            var picdt = dmmimg[i].src
            console.log(picdt);

            //小图 转 大图
            picdt = picdt.replace('-','jp-')
            // bbcode
            dmmwz=dmmwz+'[img]'+ picdt +'[/img]'
            //dmmwz=dmmwz+dmmimg[i]

        }

        //复制 剪贴板
        GM_setClipboard(dmmwz);

        //修改标题

		//alert(dmmwz);

        return;

    }
    //~~end ~~~~


    // 复制 海报图片网址 按钮 ，绑定按键点击功能
	button4.onclick = function (){

        pic_fb()

	};

    // 获取 海报大图
    function pic_fb() {

		console.log('点击了按键,复制 海报图片网');

        //获取img
        var hb1 = document.querySelector('#kdescr>img');
        var fbwz = hb1.src

        //删除 跳转网址
        fbwz = fbwz.replace('https://kp.m-team.cc/imagecache.php?url=','')

        //解码 url
        fbwz = decodeURIComponent(fbwz)

        //
        var btnr1 = fbwz;

        //复制 剪贴板
        GM_setClipboard(btnr1);


		//alert(btnr1);

        return;
    }

    //~~ button4  end ~~~~



   //~~~~~~~~~~Add Button ~~~~~~~~~~~

    //查找  H1标题前的 元素
    var x = document.getElementsByClassName('bottom')[0];

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("buttom对象:",x);

    //添加 子元素
	x.appendChild(button);
    //~~~~~~~~~end~~~~~~~


    //查找  副标题 文本 元素
    var y = document.getElementsByClassName('rowhead nowrap')[0];

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("button2对象:",y);

    //添加 子元素
	y.appendChild(button2);
    //~~~~~~~~~end~~~~~~~


    //查找  dmm 文本 元素
    var z = document.querySelector('.dmm_type');

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("button3对象:",y);

    //添加 子元素
	z.appendChild(button3);
    //~~~~~~~~~end~~~~~~~


    //查找  海报图片 元素
    var xy = document.querySelector('#kdescr');

    //在浏览器控制台可以查看所有函数，ctrl+shift+I 调出控制台，在Console窗口进行实验测试
    console.log("button4对象:",xy);

    //添加 子元素
	xy.appendChild(button4);

    //~~~~~~~~~end~~~~~~~



    // search id
    //var y = document.getElementById('s_btn_wr');
    //y.appendChild(button);


    //提取 视频 编号，去除 非中文
    function RemoveChinese(strValue) {

    //字符串 为空
    if(strValue!= null && strValue != ""){

        //控制台 输出
        console.log(strValue);

        //正则 表达式 abc-123
        var reg = /^[A-Za-z0-9]{2,8}-\d{3,7}/g;

        var wjjg = reg.exec(strValue)

        //fc-ppv-1234567 特殊 文件名
        if(wjjg == null){
            reg = /^[A-Za-z0-9]{2,8}-[A-Za-z]{3}-[0-9]{7}/g;
            wjjg = reg.exec(strValue)
            return wjjg;

        }

        //alert(wjjg)

        return wjjg;

    }
    else{
        return "";
    }
    }
        //~~~~~~~~~end~~~~~~~

})();