const fs = require('fs')
const path = require('path')

function traverseFolder(folderPath) {

  let wjm = [];

  // 读取文件夹列表
  const files = fs.readdirSync(folderPath)

  // 遍历文件夹列表
  files.forEach(function (fileName) {
    
    // 拼接当前文件路径
    const filePath = path.join(folderPath, fileName)

    // 判断该路径是文件夹还是文件
    const stats = fs.statSync(filePath)

    if (stats.isDirectory()) {
      // 如果是文件夹，递归遍历
      // traverseFolder(filePath)
    } else {

      // 如果是文件，执行操作
      console.log(filePath)

      // 数组 添加 元素
      wjm.push(filePath)
    
    }
  })

  return wjm;
}

mz1 = traverseFolder('./');

console.log("folder file name :"+mz1);

