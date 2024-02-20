document.addEventListener('DOMContentLoaded', function() {

  // 创建 文件夹 ~~~~~~~~~~~
  var createFolderButton = document.getElementById('createFolderButton');
  
  createFolderButton.addEventListener('click', async function() {

    var today = new Date();
    var year = today.getFullYear();
    var month = (today.getMonth() + 1).toString().padStart(2, '0');
    var day = today.getDate().toString().padStart(2, '0');
    var folderName = year + '_' + month + '_' + day;

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

  // ~~~~~end~~~~~~~~~~~~~~~~~




  /*

  删除 文件夹 选择器，获取不到文件夹
  
  */
  // 导出书签 网址到json~~~~~~~~~~~~~~~~~~~~~~


  var exportButton = document.getElementById('exportButton');
  var folderNameInput = document.getElementById('folderNameInput');
  var exportResults = document.getElementById('exportResults');

  exportButton.addEventListener('click', async function() {

    var folderName = folderNameInput.value.trim();

    // 如果 folderName 内容为空
    if (!folderName) {

      // 获取当前日期并更新输入框的默认值
      var today = new Date();
      var date = today.getFullYear() + '_' + (today.getMonth() + 1).toString().padStart(2, '0') + '_' + today.getDate().toString().padStart(2, '0');
      folderNameInput.value = date;
      folderName =date
      
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

    // 创建Blob对象并下载
    let blob = new Blob([JSON.stringify(bookmarksData, null, 2)], { type: 'application/json' });
    let downloadUrl = URL.createObjectURL(blob);
    let downloadLink = document.createElement('a');
    downloadLink.href = downloadUrl;
    downloadLink.download = 'bookmarks.json';
    downloadLink.textContent = 'Download Bookmarks JSON';
    downloadLink.style.display = 'block';
    exportResults.appendChild(downloadLink);
  });

  // end  导出书签 网址到json~~~~~~~~~~~~~~~~~~~~~~

});