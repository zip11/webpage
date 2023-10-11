const fs = require('fs')
const path = require('path')

// 获取 文件夹下 所有 文件 ，不包含 子文件夹
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
      // console.log(filePath)

      // 数组 添加 元素
      wjm.push(filePath)
    
    }
  })

  return wjm;
}

// 获取 视频 文件名
function videoname(mz1) {

  let flvname = [];

  // 遍历 数组
  for(var i = 0, len = mz1.length; i < len; i++) {
  
    let vname = mz1[i];
    // console.log(vname);
  
    //  获取 文件 扩展名
    let ename = path.extname(vname);
    // console.log(ename);
  
    // 判断 扩展名
    if(ename == ".flv") {

      // 加入新 数组
      flvname.push(vname);
    }
  
    
  }

  return flvname;
}

function m4a_audio(vname3) {

  // 生成 新 音频 文件名
  let aname = [] ;

  for(let vnam of vname3){

    // 获取 文件名 ，无后缀，扩展名
    let v_nam = path.parse(vnam).name + ".m4a"
    
    // 加入 音频 数组
    aname.push(v_nam);

  }

  return aname;

}

// 获取 文件夹下 所有文件
mz0 = traverseFolder('./');

// console.log("folder file name :"+mz1);

// 获取 视频文件名
let vname2 = videoname(mz0);

console.log("flvname: " + vname2 );

// 新 音频 文件名~~~~~~~~start~~~~~~

var m4afile = [];
m4afile = m4a_audio(vname2);

console.log("m4a-file:" + m4afile)

// flv 转换 m4a，批量转换 数组 -多个文件
var zh1 = require('./ffmpeg-flv');

for(var i = 0, len = m4afile.length; i < len; i++) {

  // console.log(m4afile[i]);

  // 单个 视频 转换 音频
  zh1.flvtom4a(vname2[i],m4afile[i]);
}

