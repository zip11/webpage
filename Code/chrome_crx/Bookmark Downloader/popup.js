// 当文档加载完成后，从存储中获取保存的值
document.addEventListener('DOMContentLoaded', function() {

  // 读取 游览器 存储
  chrome.storage.local.get(['passkey', 'folderName'], function(result) {

    // 保存的值，填入网页
      document.getElementById('passkey').value = result.passkey || '';
      document.getElementById('folderName').value = result.folderName || '';
  });

});

// 保存按钮事件监听器
document.getElementById('save').addEventListener('click', function() {

  // 读取 网页 密钥，到常量
  const passkey = document.getElementById('passkey').value;
  const folderName = document.getElementById('folderName').value;

  // 网页密码，保存到 持久化储存
  chrome.storage.local.set({passkey: passkey, folderName: folderName}, function() {
      console.log('Settings saved');
  });

});

// 生成下载链接按钮事件监听器
document.getElementById('generate').addEventListener('click', function() {

  // 获取 网页 密钥
  const passkey = document.getElementById('passkey').value;

  // 获取 游览器。书签。
  chrome.bookmarks.getTree(function(bookmarkTreeNodes) {

      const folder = findFolder(bookmarkTreeNodes, document.getElementById('folderName').value);
      let links = '';

      if (folder) {

          for (let bookmark of folder.children) {

              // 匹配网址 tid
              const tidMatch = bookmark.url.match(/tid=(\d+)/);

              // 匹配 网址 不为空
              if (tidMatch) {

                  // 下载网址 模板
                  const downloadLink = `https://www.f.com/t/?tid=${tidMatch[1]}&passkey=${passkey}`;
                  // 网址 加 换行符
                  links += downloadLink + '\n';
                  console.log(downloadLink);
              }
          }

          // 网页 加入 下载链接
          document.getElementById('downloadLinks').value = links;
      }
  });
});

// 寻找书签 文件夹
function findFolder(bookmarkNodes, folderName) {

  for (let node of bookmarkNodes) {

      if (node.title === folderName && node.children) {
          return node;
      } else if (node.children) {
          const found = findFolder(node.children, folderName);
          if (found) return found;
      }
  }
  return null;
}
