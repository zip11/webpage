// 函数 创建 一个文件
const fs = require('fs');

// 创建忽略 上传文件 github
function createFile(filePath, content) {
    
    // 检查文件是否存在
    if (fs.existsSync(filePath)) {
        console.log('文件已存在:', filePath);
        return;
    }
    // 创建文件
    fs.writeFile(filePath, content, (err) => {
        if (err) {
            console.error('写入文件出错:', err);
        } else {
            console.log('文件创建成功:', filePath);
        }
    });
}

// 创建文件 end ~~~~~~~~~~~~

// 复制文件夹下 所有文件 和 子文件夹下 所有文件
function copyFolderRecursive(source, target) {

    // 检查目标文件夹是否存在
    if (!fs.existsSync(target)) {
        fs.mkdirSync(target);
    }
    
    // 读取源文件夹 
    const files = fs.readdirSync(source);

    for (let i = 0; i < files.length; i++) {
        
        // 获取当前文件的完整路径
        const currentFile = path.join(source, files[i]);

        if (fs.lstatSync(currentFile).isDirectory()) {
            // 如果是文件夹，递归调用copyFolderRecursive
            copyFolderRecursive(currentFile, path.join(target, files[i]));
        } else {
            // 如果是文件，复制文件
            fs.copyFileSync(currentFile, path.join(target, files[i]));
        }
    }

}

// 复制文件夹 end ~~~~~~~~~~~~


// 读取 json ~~~~~~~~~~~~~~~~~~~~~~


// 从 JSON 文件中读取配置对象
function loadConfig() {

    try {

        // 读取 JSON 文件,同步
        const configJson = fs.readFileSync('config.json', 'utf8');

        // 解析 JSON 字符串为 JavaScript 对象
        const newConfig = JSON.parse(configJson);
        return newConfig;

    } catch (err) {

        console.error('Error reading or parsing the file:', err);
        return err;
    }
  
}

// 读取 具体 配置项
function read_json() {

    // 获取单个 配置 字符串
 
   // 读取配置文件
   const pz = loadConfig();
 
   // 获取配置文件中的属性
   let inputFolder = pz.path;
    //console.log( "input folder: " + inputFolder);
   
   return inputFolder;
 
}
// json end ~~~~~~~~~~~~~~~~~~~


/*
    


// 删除 文件夹下，node_modules的文件夹

// const fs = require('fs');
const path = require('path');

// 删除 文件夹
function deleteNodeModules(directory) {

    // directory replace \ to /
    directory = directory.replace(/\\/g, '/');
   
    
    const nodeModulesPath = path.join(directory, 'node_modules');

    if (fs.existsSync(nodeModulesPath)) {

        // 删除文件夹及其内容
        fs.rmSync(nodeModulesPath, { recursive: true });
        console.log(`Deleted ${nodeModulesPath}`);

    } else {
        console.log(`${nodeModulesPath} does not exist.`);
    }
}

/*
console.log('github upload folder,Start deleting node_modules...');

// 使用同步程序，键盘输入字符串
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('input folder path for upload github folder:', (answer) => {

    rl.close();


    // 调用函数删除node_modules文件夹
    // console.log(answer);
    deleteNodeModules(answer);

});

*/

// 读取josn
var lj1 = read_json();

lj1 = lj1.replace(/\\/g, '/');
console.log(`json read path : ${lj1}`);

// st input
console.log('Start disable upload node_modules...');


// console.log(readjson('config.json'));

// 键盘输入字符串
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('input folder path for upload github folder:', (answer) => {

    rl.close();

    //创建 忽略 上传 文件
    let directory = path.join(answer, '.gitignore');
    createFile(directory, 'node_modules/\nconfig.json');


    // console.log(answer);
    // 复制 文件夹 到 github 文件夹
    copyFolderRecursive(answer, lj1);

    console.log('End disable upload node_modules...');

});



