## js创建悬浮按钮  ##

    let mybtn = document.createElement('button');

    document.body.appendChild(mybtn);

    mybtn.id = 'my-btn';

    mybtn.innerHTML = `按钮
    <style>
    #my-btn {
	    /* position设置为fixed，固定位置，即使窗口滚动位置不变 */
	    position: fixed;
	    top: 100px;
	    left: 30px;
	    width: 150px;
    }
    </style>`

    mybtn.onclick = function () {

	    alert(mybtn.innerText)

    }