// ==UserScript==
// @name         Mt-collection-add-number
// @namespace    your-namespace
// @version      0.1
// @description  下载文件名，为指定的类名元素添加数字序号
// @author       4-22
// @match        https://kp.m-team.cc/browse/adult?onlyFav=1
// ==/UserScript==

(async function() {

    'use strict';

    function sleep(time) {
        return new Promise(resolve => setTimeout(resolve, time));
    }

    // 保存内容到 txt 文件并下载
    function saveContentToTxt(content) {
        // 创建 Blob 对象
        var blob = new Blob([content], {type: 'text/plain'});

        // 创建 URL 对象并生成下载链接
        var url = URL.createObjectURL(blob);

        // 创建下载链接并点击下载
        var downloadLink = document.createElement('a');
        downloadLink.href = url;
        downloadLink.download = 'numbered_content.txt';
        downloadLink.click();
    }




    // 定义一个函数，将数组所有元素存入一个 JSON 文件并提供下载链接
    function saveArrayToJSONFile(contentArray) {

        // 构建要写入文件的内容，将数组内容存入 JSON 对象
        var jsonData = { contentArray: contentArray };

        // 将 JSON 对象转换为字符串
        var jsonString = JSON.stringify(jsonData, null, 2);

        // 创建 Blob 对象
        var blob = new Blob([jsonString], {type: 'application/json'});

        // 创建下载链接并添加到页面中
        var downloadLink = document.createElement('a');
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.download = 'content.json';
        downloadLink.textContent = '下载 content.json';
        downloadLink.style.display = 'block'; // 使下载链接换行显示
        document.body.appendChild(downloadLink);
        
        downloadLink.click();
    }


    // 定义一个函数，用于提取字符串中的 "abcd-1234" 部分

    function extractPatternFromString(inputString) {

        // 使用正则表达式匹配符合格式的部分
        var match = inputString.match(/[a-zA-Z]+-\d+/);
        if (match) {
            return match[0]; // 返回匹配到的部分
        } else {
            return null; // 如果没有匹配到则返回 null
        }
    }


    function add_number() {

        console.log("start!!")

        // 获取具有类名为 ".ant-table-cell.px-5px.ant-table-cell-ellipsis.ant-table-cell-row-hover" 的所有元素
        var elements = document.querySelectorAll('.ant-row.ant-row-no-wrap');
  
        // 初始化序号
        var index = 1;

        // 保存内容的数组
        var contentArray = [];  

        // 遍历每个匹配的元素
        elements.forEach(function(element) {

            // 检查元素内容是否为空白
            var content = element.textContent.trim();

            if (content !== '') {

                // 如果内容不为空白，则添加数字序号并替换原始内容
                var numberedContent = index + '. ' + content;
                // console.log(numberedContent)
                // element.textContent = numberedContent;

                // 提取 视频 编号
                numberedContent = extractPatternFromString(numberedContent)

                // 检查元素内容 不 为 null
                if(numberedContent !== null){

                    // 编号 加入 数组
                    contentArray.push(numberedContent);

                    // 序号 +1 
                    index++;

                }

            }

        });

        // var jsonContent = arrayToJSON(contentArray);
        // console.log("json",jsonContent)

        saveArrayToJSONFile(contentArray);


        // saveJSONToFile(jsonContent);
        

        // txt file  ~~~~~
        // 将内容数组转换为字符串
        // var contentString = contentArray.join('\n');

        // 保存内容到 txt 文件并下载
        // saveContentToTxt(contentString);
    }


    // ~~~~~~~~~~ sleep wait ~~~~~~~~~~

    // 等待1秒    
    await sleep(8000);  

    add_number();

    // ~~~~~~~~~observeElement 

    // 当目标元素加载后将被调用
    function observeElement(className, callback) {

        // 创建一个观察器实例并传入一个回调函数
        const observer = new MutationObserver(function(mutations, me) {
            // 查找页面上带有指定类名的元素
            const element = document.querySelector(className);
            if (element) {
                callback(element); // 调用回调函数
                me.disconnect(); // 停止观察
                return;
            }
        });

        // 开始观察文档对象模型（DOM）的变化，配置对象指定了我们想要观察的变化类型
        observer.observe(document.documentElement, {
            childList: true,
            subtree: true
        });
    }

    // 目标元素加载后将被调用的函数
    function onElementLoaded(element) {

        console.log('元素加载完成:', element);
        // 添加 文件 标题 序号
        add_number();

    }

    // 调用封装好的函数，传入目标元素的类名和回调函数
    // observeElement('.ant-row.ant-row-no-wrap', onElementLoaded);



})();
