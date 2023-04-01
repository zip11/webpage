"eslint.codeActionsOnSave.rules": null
}




ESlint用于检查js语法错误






### 本地安装 ###

只安装当前项目文件夹

npm install eslint


### 全局安装 ###
npm install -g eslint




## 安装404错误，配置镜像库网站 ##

npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/ESLint - Not found

国内cnpm淘宝镜像

npm config set registry https://registry.npm.taobao.org/

查看当前的代理设置

npm config get registry


## 创建配置文件 ##

在新文件夹上，您可能还需要创建一个.eslintrc配置文件。您可以通过使用VS Code命令创建ESLint配置或在终端中运行ESLint命令来实现这一点。如果您已经全局安装了ESLint（见上文），那么在终端中运行ESLint-init。

如果您已经在本地安装了ESLint，

--在Windows和下的

 .\node_modules\.bin\eslint --init

——Linux和Mac下的init。

./node_modules/.bin/eslint --init



执行“禁用ESLint”命令来禁用工作区文件夹的ESLint。

Disable ESLint
