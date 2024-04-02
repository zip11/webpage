// 生成日期字符串的函数
function generateDateString(date) {
  var year = date.getFullYear();
  
  // 将月份和日期转换为字符串，并确保两位数，例如将单个数字的月份或日期前面添加零
  var month = (date.getMonth() + 1).toString().padStart(2, '0'); // 月份从0开始，因此需要加1
  var day = date.getDate().toString().padStart(2, '0'); // 获取日期并确保是两位数

  return year + '_' + month + '_' + day;
}

document.addEventListener('DOMContentLoaded', function() {

  // 创建 文件夹
  var createFolderButton = document.getElementById('createFolderButton');

  createFolderButton.addEventListener('click', async function() {

    var today = new Date();
    var folderName = generateDateString(today);

    // 检查文件夹是否存在
    let folders = await chrome.bookmarks.search({title: folderName});

    if (folders.length === 0) {
      // 文件夹不存在，创建它
      await chrome.bookmarks.create({
        title: folderName
      });

      // 提示用户操作成功
      alert('Folder "' + folderName + '" created successfully.');
    } else {
      // 文件夹已存在，提示用户
      alert('Folder "' + folderName + '" already exists.');
    }

  });

  // 导出书签 网址到json
  var exportButton = document.getElementById('exportButton');
  var folderNameInput = document.getElementById('folderNameInput');
  var exportResults = document.getElementById('exportResults');

  exportButton.addEventListener('click', async function() {

    var folderName = folderNameInput.value.trim();

    // 如果 folderName 内容为空
    if (!folderName) {
      // 获取当前日期并更新输入框的默认值
      var today = new Date();
      folderNameInput.value = generateDateString(today);
      folderName = folderNameInput.value;
    }

    // 检查文件夹是否存在
    let folders = await chrome.bookmarks.search({title: folderName});
    if (folders.length === 0) {
      exportResults.textContent = 'Folder not found.';
      return;
    }

    // 获取所选文件夹的书签
    let bookmarks = await chrome.bookmarks.getChildren(folders[0].id);

    // 创建JSON数据
    let bookmarksData = bookmarks.map(bookmark => {
      return {
        title: bookmark.title,
        url: bookmark.url
      };
    });

    var folderNameWithExtension = 'bookmarks_' + folderName + '.json';

    // 创建Blob对象并下载
    // 创建包含书签数据的 Blob 对象，类型为 JSON
    let blob = new Blob([JSON.stringify(bookmarksData, null, 2)], { type: 'application/json' });

    // 使用 Blob 对象创建一个 URL
    let downloadUrl = URL.createObjectURL(blob);

    // 创建一个 <a> 元素作为下载链接
    let downloadLink = document.createElement('a');

    // 设置下载链接的 href 属性为 Blob URL
    downloadLink.href = downloadUrl;

    // 设置下载链接的下载文件名
    downloadLink.download = folderNameWithExtension;

    // 设置下载链接的文本内容
    downloadLink.textContent = 'Download Bookmarks JSON';

    // 设置下载链接的样式为块级元素，使其单独占据一行
    downloadLink.style.display = 'block';

    // 将下载链接添加到 exportResults 元素中显示在界面上
    exportResults.appendChild(downloadLink);

  });

});
