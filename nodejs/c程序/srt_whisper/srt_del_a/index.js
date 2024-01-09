// 搜索文件夹下 所有srt文件，删除 啊 字符

// 删除 单个 srt 文件 ，啊字符
function remove_srt_a (srtfile) {

    const fs = require('fs');
    const path = require('path');
    
    // 读取 SRT 文件内容
    fs.readFile(path.resolve(__dirname, srtfile), 'utf-8', (err, data) => {
      
        if (err) {
        console.error('Error reading file:', err);
        return;
      }
    
      // 使用正则表达式替换连续的 "啊" 字符串为单个 "啊" 字符
      const cleanedData = data.replace(/啊/g,'');

      // 新建 srt 文件名
      // let new_srtfile = srtfile.replace('.srt', '_zh.srt');

      // 使用旧文件名，复制旧文件
      let new_srtfile = srtfile;

      // 将修改后的内容写入新的 SRT 文件
      fs.writeFile(path.resolve(__dirname, new_srtfile), cleanedData, 'utf-8', (err) => {
        
        if (err) {
          console.error('Error writing file:', err);
        } else {
          console.log('Srt File cleaned and saved');
        }
    
      });
    });
}



//遍历获取文件夹下 所有srt 文件


function remove_srt_a_in_folder(folderPath) {

  const fs = require('fs');
  const path = require('path');

  fs.readdir(folderPath, (err, files) => {

    if (err) {
      console.error('Error reading folder:', err);
      return;
    }
    
    files.forEach(file => {

      if (path.extname(file) === '.srt') {

        console.log('srt file:', file);

        // 删除 单个字幕 文件，内容中的 啊
        // remove_srt_a();

      }

    });
  });
}

// 键盘输入 文件夹路径
const readline = require('readline-sync'); 
let name = readline.question("input srt folder:"); 


// 调用函数并传入文件夹路径
remove_srt_a_in_folder(name);