// 使用ffmpeg批量压缩文件夹内的jpg文件，分辨率是原始分辨率的1/2

const ffmpeg = require('ffmpeg');
const path = require('path');
// Import the filesystem module 
const fs = require('fs')



// 定义一个函数，用于压缩图片
const sharp = require('sharp');

// 用于压缩 单个图片
function compressImage(inputPath, outputPath) {
 sharp(inputPath)
   .metadata((err, metadata) => {

     if (err) {
       console.error('Error getting image metadata:', err);
     } else {
       console.log('Image metadata:', metadata);

      // 获取原始分辨率的 1/2
       const newWidth = Math.floor(metadata.width / 2); 
       const newHeight = Math.floor(metadata.height / 2);
       
       // 
       if( metadata > 6000) {

        // 压缩图片到原始分辨率的 1/2
        sharp(inputPath)
        
        .resize(newWidth, newHeight)
        
        .toFile(outputPath, (err, info) => {
        
        if (err) {
            console.error('Error compressing image:', err);
          } else {
            console.log('Image compressed successfully:', info);
          }

          });
        } else{

         // 使用sharp库进行图片压缩,不降低 分辨率

          sharp(inputPath)
          
          .toFile(outputPath, (err, info) => {
          
          if (err) {
              console.error('Error compressing image:', err);
            } else {
              console.log('Image compressed successfully:', info);
            }

          });

        }


      }
   })

   /*
   .toFile('output.jpg', (err, info) => {

     if (err) {
       console.error('Error saving image:', err);
     } else {
       console.log('Image saved successfully:', info);
     }

   });

   */

}





// 定义一个函数，用于压缩文件夹中的图片
function compressFolder(inputFolder, outputFolder) {

    // 读取文件夹中的文件
  const files = fs.readdirSync(inputFolder);

  // 遍历文件夹中的文件
  files.forEach(file => {
    
    // 获取文件的输入路径
    const inputPath = path.join(inputFolder, file);
    
    // 获取文件的输出路径
    const outputPath = path.join(outputFolder, file);
    
    // 判断文件是否为jpg格式
    if (file.endsWith('.jpg')) {
    
      // 调用compressImage函数，压缩文件
      compressImage(inputPath, outputPath)
            

    }

  });

}

function save_json(string1) {


  // 更新配置文件中的属性

  fs.writeFileSync('config.json', JSON.stringify(config));

  // JSON.stringify() 是一个内置的 JavaScript 函数，
  //用于将 JavaScript 对象转换为 JSON 字符串。
  
  console.log('配置文件已更新。' + JSON.stringify(config));

}

// 从 JSON 文件中读取配置对象
function loadConfig() {

  const configJson = fs.readFileSync('config.json', 'utf8');
  const newConfig = JSON.parse(configJson);
  return newConfig;

}

// 按键 字符串 输入
function prompt(string2) {
  
  const readline = require('readline-sync'); 
  
  let name = readline.question(string2); 
  // console.log("输入内容"+name);

  return name;
  
}

function jpg_encode(inputFolder2, outputFolder2) {

  //windows路径转换
  inputFolder2 = inputFolder2.replace(/\\/g, '/');
  outputFolder2 = inputFolder2 + "_encode";

  // 检查输出文件夹是否存在，如果不存在则创建
  if (!fs.existsSync(outputFolder2)) {
    fs.mkdirSync(outputFolder2);
  }


  // 压缩 文件夹 图片
  compressFolder(inputFolder2, outputFolder2);
  console.log('Compression completed.');
  
}

function save_path() {

  //按键输入路径，保存到 inputpath
  let inputFolder3 = prompt("input picture folder path:");


  // 替换反斜杠为正斜杠
  const inputFolder4 = inputFolder3.replace(/\\/g, '/');

  // 更新配置文件中的属性
  config.inputFolder = inputFolder4;

  // 保存配置对象到config.json
  save_json(config)

}

function save_path_noin() {


  // 更新配置文件中的属性
  config.inputFolder = "";

  // 保存配置对象到config.json
  save_json(config)

}

// ~~~~start~~~~~~~

console.log("jpg图片压缩——程序 启动！！！");

// json配置  对象
var config = {

  inputFolder: '',
};

// 判断config.json是否存在，如果没有就新建config.json

if (!fs.existsSync('config.json')) {
  
  // 保存配置对象到config.json
  save_path(config);

} else{

  // 读取配置文件
  const pz = loadConfig();

  // 获取配置文件中的属性
  let inputFolder = pz.inputFolder;
  console.log( "input folder: " + inputFolder);

  // inputFolder，不为空
  if (inputFolder != "") {

    const outputFolder = inputFolder + "_encode";
    console.log( "output folder: " + outputFolder);

    jpg_encode(inputFolder, outputFolder);

    // 清空路径

    save_path_noin() ;

    console.log("图片压缩结束！！！");

  } else{

    save_path();
    
  }

}


