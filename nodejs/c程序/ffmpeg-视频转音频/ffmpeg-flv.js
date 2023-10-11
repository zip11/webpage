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

module.exports = {flvtom4a}

let fname3 = "te.flv"
let aname3 = "te.mp3"

// 视频flv 转 音频m4a
// flvtom4a(fname3,aname3);