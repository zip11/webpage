// 视频 转 音频 ffmpeg

async function flvtom4a(fname,aname) {

    var ffmpeg = require('fluent-ffmpeg');
    
    await ffmpeg(fname)
        
        .output(aname)
        .noVideo()
    
        /*
        .outputOptions([
            '-c:a copy'
          ])
    
        */
        
        .audioCodec('copy')
    
        .on('error', function(err) {
        console.log('An error occurred: ' + err.message);
        })
        
        .on('end', function() {
            console.log('Processing finished !');
        })

        .on('progress', function(progress) {
            console.log('Processing: ' + progress.percent + '% done')
        })
        
        .run();

}

// module.exports = {flvtom4a}

// let fname3 = "te.flv"
// let aname3 = "te.mp3"

// 视频flv 转 音频m4a
// flvtom4a(fname3,aname3);

const readline = require('readline-sync'); 
let videopath = readline.question("输入 MP4 路径：");

// 替换双引号
videopath = videopath.replace(/"/g, '');


const path = require('path');
// 替换 路径分隔符
videopath = videopath.split(path.sep).join('/');
console.log(videopath);

// 生成 音频 文件名
const audiofile = videopath.replace(/.mp4|.MP4/g,'.m4a')
console.log(audiofile);

flvtom4a(videopath,audiofile);
// 正则表达式 /mp4|MP4/g 匹配字符串中的 mp4 或 MP4，g 标志表示全局