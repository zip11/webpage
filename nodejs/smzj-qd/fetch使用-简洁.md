安装 node-fetch:

    npm install node-fetch

使用 fetch 之前先加载：

    const fetch = require('node-fetch')
    

简单使用方法：

    fetch('https://api.github.com/users/github')
	    .then(res => res.json())
	    .then(json => console.log(json));

————————————————

原文链接：https://blog.csdn.net/henryhu712/article/details/87775497