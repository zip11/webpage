nodejs_视频转换使用_fluent-ffmpeg模块


nodejs控制ffmpeg，使用 fluent-ffmpeg 模块

## 安装模块 ##

    npm install fluent-ffmpeg

## 测试程序例子 ##

//视频MP4 转 音频m4a, 复制音频，无损转换

    var ffmpeg = require('fluent-ffmpeg');
    
    ffmpeg('1.mp4').output('1.m4a')
    .noVideo()
    .audioCodec('copy')
    .run();

// 视频MP4 转 音频mp3，有损转码

    var ffmpeg = require('fluent-ffmpeg');
    
    ffmpeg('1.mp4').output('1.mp3')
    .noVideo()
    .format('mp3')
    .outputOptions('-ab','192k')
    .run();

