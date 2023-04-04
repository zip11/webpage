## 为什么要使用npm init初始化项目 ##

在node开发中使用npm init会生成一个pakeage.json文件，这个文件主要是用来记录这个项目的详细信息的，它会将我们在项目开发中所要用到的包，以及项目的详细信息等记录在这个项目中。方便在以后的版本迭代和项目移植的时候会更加的方便。也是防止在后期的项目维护中误删除了一个包导致的项目不能够正常运行。使用npm init初始化项目还有一个好处就是在进行项目传递的时候不需要将项目依赖包一起发送给对方，对方在接受到你的项目之后再执行npm install就可以将项目依赖全部下载到项目里。话不多说我们就直接开始进行操作。

## 执行npm init ##

执行npm init是需要在DOS窗口执行的，我们可以windows+r键来打开窗口，然后输入CMD执行，然后就可以打开DOS窗口了。打开窗口之后，在DOS窗口中进入自己项目所在的目录。


直接执行npm init,执行了npm init之后,会让我们填写一些配置信息，如果还不知道怎么填写的话可以一路回车


    package name:  你的项目名字叫啥
    version:  版本号
    description:   对项目的描述
    entry point:  项目的入口文件（一般你要用那个js文件作为node服务，就填写那个文件）
    test command: 项目启动的时候要用什么命令来执行脚本文件（默认为node app.js）
    git repository:如果你要将项目上传到git中的话，那么就需要填写git的仓库地址（这里就不写地址了）
    keywirds：   项目关键字（我也不知道有啥用，所以我就不写了）
    author: 作者的名字（也就是你叫啥名字）
    license:发行项目需要的证书（这里也就自己玩玩，就不写了）

## 修改package.json文件 ##

如果我们在进行package.json文件配置的时候写错了东西，或者后期要添加什么内容的话，我们是可以直接在项目的根目录中打开然后进行修改，我在配置文件中增加了一个运行项目的命令

    //package.json
    {
      "name": "xajd",
      "version": "1.0.0",
      "description": "我的第一个node项目",
      "main": "app.js",
      "dependencies": {
	    "koa": "^2.0.0",
	    "koa-router": "^7.4.0",
	    "mysql": "^2.17.1"
      },
      "devDependencies": {},
      "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1",
	    "start": "node app.js"//这个是我加入的一个配置，在窗口中执行npm start会自动执行start中的命令
      },
      "author": "wudi",
      "license": "ISC"
    }


## 启动项目 ##

 npm start
