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


Cannot use import statement outside a module

 import 关键字是 ES6 的一个特性，而 nodejs 默认场景下是支持 AMD，CommonJS,

首先我们可确认的是我们使用到了一个模块 node-fetch，而在 nodejs 中对于模块的调用方式有两种，分别对应 ES5 规范 和 ES6 规范，其中 ES5 规范对应的是 require 函数，通过调用 require 函数的方式引入模块;而 ES6 规范引入了 import 关键字，通过该关键字引入模块。

    // ES5 的模块引入方式
    const fetch = require("node-fetch");
    
    // ES6 的模块引入方式
    import fetch from "node-fetch";


node demo01.js 的方式执行代码的话，是一种非模块话的方式调用，在这种调用方式下无法直接使用 import 关键字。

如果要使用的话，需要在 package.json 文件中指定当前工程是一个模块，在能够在模块中使用 import 关键字。


import 方式执行代码

首先确认下import 方式引入 node-fetch 是在 node-fetch 的最新版本 v3.x出现的，而 node-fetch 的 v3.x 版本要求 nodejs版本大于 12.20.0。


----------


这里说明一下 package.json 是一个包配置文件,可以由 npm init 在当前工程的根目录下自动生成，也可以自己手动编写。

npm 通过该配置文件可以实现对该工程中依赖的模块进行管理，比如希望在当前工程中添加对 node-fetch的依赖，

- 首先使用 npm init 在当前目录下创建 package.json 文件，

- 然后执行命令 npm install node-fetch --save 就会将对 node-fetch的依赖写入到 package.json 中。


现在我们有了 package.json ,我们尝试按要求往里面添加一个 "type":"module",标记当前工程为一个模块：



----------


 node-fetch版本升级的问题，也就是 node-fetch存在一个大的版本升级，具体点讲就是node-fetch从 v2.x 升级到 v3.x 的时候，其引入方式存在着大的更新，从之前的 require 修改为了 import ，并且要求 nodejs 版本需要大于 12.20.0。


    # 查看 node-fetch 信息
    npm info node-fetch
    # 查看 node-fetch 所有版本
    npm view node-fetch versions
    # 安装 node-fetch 并指定版本为 2.6.2
    npm install node-fetch@2.6.2


----------

————————————————
版权声明：本文为CSDN博主「ghimi」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_19922839/article/details/120276900