// ==UserScript==
// @name         yt Video Links
// @namespace    yt-video-link
// @version      0.1
// @description  Export video links from specific webpage to JSON file
// @author       24-3-6
// @match        https://www.youtube.com/*/videos
// ==/UserScript==

(function() {


    'use strict';

    window.addEventListener('load', function() {

        // 在页面完全加载后执行你的脚本代码
        // 例如：
        console.log('YouTube page fully loaded!');
        // 这里添加你的其他脚本逻辑...


        // 获取当前日期
        var currentDate = new Date();
        var year = currentDate.getFullYear();
        var month = ('0' + (currentDate.getMonth() + 1)).slice(-2);
        var day = ('0' + currentDate.getDate()).slice(-2);
        var formattedDate = year + '-' + month + '-' + day;

        // 获取所有具有 id="video-title-link" 属性的 <a> 元素
        var videoLinks = document.querySelectorAll('a[id="video-title-link"]');
        var videoData = [];

        // 遍历所有符合条件的 <a> 元素，获取 href 和 title，并添加到 videoData 数组中
        videoLinks.forEach(function(link) {
            var href = link.href;
            var title = link.title;
            videoData.push({ href: href, title: title });
        });

        // 将 videoData 转换为 JSON 格式，并美化输出
        var jsonData = JSON.stringify(videoData, null, 2);

        // 创建一个 Blob 对象来保存 JSON 数据
        var blob = new Blob([jsonData], {type: 'application/json'});

        // 创建一个 <a> 元素来触发下载 JSON 文件
        var a = document.createElement("a");
        var url = URL.createObjectURL(blob);
        a.href = url;
        a.download = 'video_links_' + formattedDate + '.json'; // 添加日期到文件名中
        document.body.appendChild(a);
        a.click();

        // 清理创建的 <a> 元素和 URL 对象
        document.body.removeChild(a);
        URL.revokeObjectURL(url);


    });



})();
