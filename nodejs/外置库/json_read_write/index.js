// Import the filesystem module 
const fs = require('fs')

// 写入 json ~~~~~~~~~~~~~~~~~~~~~~

// 按键 字符串 输入
function prompt(string2) {

    const readline = require('readline-sync'); 

    let name = readline.question(string2); 
    // console.log("输入内容"+name);

    return name;
    
}

function save_json(string1) {


    // 更新配置文件中的属性
  
    fs.writeFileSync('config.json', JSON.stringify(config));
  
    // JSON.stringify() 是一个内置的 JavaScript 函数，
    //用于将 JavaScript 对象转换为 JSON 字符串。
    
    console.log('配置文件已更新。' + JSON.stringify(config));
  
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
   console.log( "input folder: " + inputFolder);
   
   return inputFolder;
 
}

// 程序 开始 ~~~~~~~~~~~~~~~~~~~

// json配置  对象
var config = {

    inputFolder: '',
};
  
// 判断config.json是否存在，如果没有就新建config.json
  
if (!fs.existsSync('config.json')) {

    // 保存配置对象到config.json
    save_path(config);
  
} else {

    // 读取 json ，单个配置 字符串
    read_json();
}