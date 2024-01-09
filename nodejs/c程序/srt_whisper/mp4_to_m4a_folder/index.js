// 视频 转 音频 ffmpeg

async function mp4tom4a(fname,aname) {

    console.log("m4a_start:");

    var ffmpeg = require('fluent-ffmpeg');
    
    await ffmpeg(fname)
        
        
        .noVideo()
    
        .audioCodec('copy')

        .output(aname)
    
        .on('error', function(err) {
        console.log('An error occurred: ' + err.message);
        })
        
        .on('end', function() {
            console.log('Processing finished !');
        })

        .on('progress', function(progress) {
            // console.log('Processing: ' + progress.percent + '% done')
            progressbar(progress.percent);
        })
        
        .run();

}



// 覆写 百分比 字符串
function progressbar (percent_number) {

    var log = require('single-line-log').stdout;
    
    percent_number = Math.floor(percent_number);

    log(`processing:${percent_number}%done`);
    
}

// 判断 文件是否存在
function fileexists(fname) {

    const fs = require('fs');
    const filePath = fname;

    if (fs.existsSync(filePath)) {
      
      console.log(`文件 ${filePath} 已存在,跳过转换`);
      return false;

    } else {

      console.log(`文件 ${filePath} 不存在,进行转换`);
      return true;

    }

}

// 搜索 文件夹中 和 子文件夹中 MP4

function mp4search(dir,subfolder) {

    var fs = require('fs');
    var path = require('path');

    // 读取目录 下 文件
    var files = fs.readdirSync(dir);

    for (var i in files) {

        // 拼接 全路径
        var fname = path.join(dir, files[i]);

        //获取文件信息
        var stat = fs.statSync(fname);

        // 如果stat存在，且stat是一个目录,且 搜索子文件夹 subfolder
        if (stat && stat.isDirectory() && subfolder) {

            // 如果是目录，则递归调用mp4search函数
            mp4search(fname,true);


        } else {

            // 如果文件名以.mp4结尾
            if (path.extname(fname) === '.mp4') {

                //判断path 文件名不存在 "-C", -c视频有 内嵌字幕
                if (fname.indexOf('-C') == -1) {
                
                    // 将文件名中的.mp4替换为.m4a
                    var aname = fname.replace('.mp4','.m4a');

                    // 调用flvtom4a函数，将.mp4文件转换为.m4a文件
                    console.log(`vfile_conversion_afile: ${fname} ==>  ${aname}`);

                    // 判断 音频文件 是否存在
                    if (fileexists(aname)) {
                        
                        // MP4 转换 m4a
                        mp4tom4a(fname,aname);
                    }
                }

            }

        }

    }
}



// 读取 json start ~~~~~~~~~~~~~~~~~~~~~~


// 从 JSON 文件中读取配置对象
function loadConfig() {

    // 引入 fs 模块
    const fs = require('fs');
    
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
   console.log( "input folder: " + inputFolder);
   
   return inputFolder;
 
}
// 读取 json end ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


console.log("视频mp4 转 音频m4a start");

const readline = require('readline-sync'); 
let videopath = readline.question("输入 MP4 路径：");


// 文件路径 处理 start ~~~~~~~~

// 替换双引号
videopath = videopath.replace(/"/g, '');
// 删除字符串中最后一个反斜杠,  $ 表示匹配字符串的结尾
videopath = videopath.replace(/\\$/, '');


const path = require('path');
// 替换 路径分隔符
videopath = videopath.split(path.sep).join('/');
console.log(videopath);

// 文件路径 处理 end ~~~~~~~~~~~~~~~

// 读取 json  
const folder_subfolder = read_json();

// 判断 搜索子文件夹MP4，或者 文件夹 MP4
if(folder_subfolder === "subfolder")
{
    // 遍历 子文件夹 MP4
    console.log("遍历 子文件夹 MP4");
    mp4search(videopath,true);

}
else
{
    // 只搜索 文件夹 中 MP4
    console.log("只搜索 文件夹 中 MP4");
    mp4search(videopath,false);
}   



/*

// 搜索 MP4 文件 ~start~~~~~~~~~~~
const fs = require('fs');
const folderPath = videopath; // 指定文件夹路径

// 读取 目录 下文件
const files = fs.readdirSync(folderPath);

// 过滤mp4 文件
const mp4Files = files.filter(file => {
 return path.extname(file).toLowerCase() === '.mp4';
});

console.log(mp4Files);

// mp4 end ~~~~~~~~~~~~~~



// foreach mp4Files start ~~~~~~~~~

mp4Files.forEach(function(mp4File) {

    // 获取 m4a 文件名
    let audiofile = mp4File.replace(/.mp4|.MP4/g,'.m4a')
    console.log(audiofile);

    // 拼接 mp4 文件路径
    mp4File = path.join(folderPath, mp4File);
    audiofile = path.join(folderPath, audiofile);

    // 调用 flvtom4a 函数
    console.log("mp4File: ${mp4File} to audiofile: ${audiofile} start->");

    // video to audio
    flvtom4a(mp4File,audiofile);

});

//  end ~~~~~~~~~~~~

*/

console.log("视频flv 转 音频m4a end");

