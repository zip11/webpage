
(function() {
  // 开始从哪一个MJJ开始访问，论坛的UID
  const userIdStart = 1

  // 最多访问几个MJJ
  const maxCheckNum = 10

  // 访问一个MJJ后，休息几秒
  const restSeconds = 3


  let counting = 0

  autoCheckIn()

  function autoCheckIn() {
    const userProfileUrl = `https://hostloc.com/space-uid-${userIdStart + counting++}.html`

    console.log(`fen wen ${counting}个MJJ: ${userProfileUrl}`)

    const img = new Image()
    img.src = userProfileUrl   
   
    if (counting < maxCheckNum) {
      setTimeout(autoCheckIn, restSeconds * 1000)
    }
  }
})()
EOF