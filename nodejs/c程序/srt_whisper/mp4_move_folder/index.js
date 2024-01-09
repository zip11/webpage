// Import the filesystem module 
const fs = require('fs')


// 读取 json ~~~~~~~~~~~~~~~~~~~~~~


// 从 JSON 文件中读取配置对象
function loadConfig() {

    const configJson = fs.readFileSync('config.json', 'utf8');
    const newConfig = JSON.parse(configJson);
    return newConfig;
  
}

function read_json() {

    // 获取单个 配置 字符串
 
   // 读取配置文件
   const pz = loadConfig();
 
   // 获取配置文件中的属性
   let inputFolder = pz.inputFolder;
//    console.log( "input folder: " + inputFolder);
   
   return inputFolder;
 
}
// json end ~~~~~~~~~~~~~~~~~~~


// 程序 开始 ~~~~~~~~~~~~~~~~~~~



// 文件扩展名 变量
var fileext = "";

// 读取json
fileext = read_json();

// fileext = process.argv[2];

console.log(`<文件 ${fileext} 移动 到上一层 文件夹,程序 开始>
[修改config.json，改变移动文件扩展名 ${fileext}]`);

// json配置  对象
var config = {

    inputFolder: '',
};

/*
// 读取 json，文件夹的 路径
let videopath = read_json();

console.log("videopath: " + videopath);
*/

// 读取 用户输入的 文件夹路径 st ~~~~~~~~~
const readline = require('readline-sync');

console.log(`请输入 ${fileext} 文件夹 路径:`);
let videopath = readline.question("");


// 路径处理 start ~~~~~~~~~~~~~~~~

// 删除 路径末尾的 空格
videopath = videopath.replace(/\\\s*$/g, '');

const path = require('path');

// 源文件夹路径
const sourceDir = videopath;

// 空的 文件夹  名字
const newkong = 'kong';
// 存放空文件夹 的  文件夹路径
const targetDir = path.join (videopath,newkong)

// create targetDir 
fs.mkdirSync(targetDir, { recursive: true });
//其中 recursive: true 表示在创建目录时,如果父目录不存在,将会递归地创建父目录。


// 搜索文件夹 -视频 ~~~~~~~开始~~~~~~~~
 

// 获取源文件夹下的所有文件和文件夹
const files = fs.readdirSync(sourceDir);

// 遍历文件夹下的所有文件和文件夹
for (const file of files) {

 // 获取文件的完整路径
 const filePath = path.join(sourceDir, file);

 // 如果文件是子文件夹
 if (fs.lstatSync(filePath).isDirectory()) {

   
    // 获取子文件夹下的所有 fileext 文件
   const videos = fs.readdirSync(filePath).filter(video => path.extname(video).toLowerCase() === fileext);

   // 将子文件夹下的所有视频文件移动到上一级文件夹
   videos.forEach(video => {

     // 获取视频文件的 完整路径
     const videoPath = path.join(filePath, video);
     // 获取视频文件的 目标路径
     const targetVideoPath = path.join(sourceDir, video);
     
     // 移动视频文件
     fs.renameSync(videoPath, targetVideoPath);

     console.log(`Moved file ${video} to ${sourceDir}`);

    });

    // 移动文件夹 不能是 空文件夹 名字    ~~~~~~~~~~
   if (file!== newkong) {

    // 将子文件夹移动到  空 文件夹
    const targetPath = path.join(targetDir, file);
    // 移动文件夹
    fs.renameSync(filePath, targetPath);
    
    console.log(`Moved folder ${file} to ${targetDir}`);

   }
 }
};

// 空文件夹 大小



// 搜索文件夹 -视频 ~~~~~~~结束~~~~~~~~

console.log(`文件 ${fileext} 子文件夹 处理完成！`);

