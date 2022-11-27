# insertBefore() #

方法,可以实现把一个新元素插入到现在元素的前面，与现有元素形成兄弟关系。

        var box = document.querySelector(".box");

		var p = document.createElement('p');
		p.innerHTML = "最新选项";

		box.parentNode.insertBefore(p, box);//在box之前添加元素
		// box.parentNode.insertBefore(p, box.nextSibling);//在box之后添加元素


parentElement.insertBefore(newElement,targetElement);

1、新元素，你想插入的新元素（newElement）

2、目标元素，你想把新元素插入到哪个元素的前面（targetELement）

3、父元素，目标元素的父元素（parentElement）


----------


# appendChild()  #

 方法向节点添加最后一个子节点。

    const text = document.createTextNode("Welcome to My channel");
    const pNode = document.getElementById("p");
    pNode.appendChild(text);