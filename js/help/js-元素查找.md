# document.getElementById #

返回对拥有指定 ID 的第一个对象的引用。

document.getElementById("demo");



# getElementsByTagName #

getElementsByTagName()：方法的用途是寻找有着给定标签名的所有的元素。
这个方法返回一个节点的集合，这个集合可以当做一个数组来处理。

var paras = document.getElementsByTagName("p");
for ( var i=0;i<paras.length;i++ ) {
    paras[i].setAttribute("title","");      
}

# querySelectorAll #

// 获取文档中所有 class="example" 的 <p> 元素
var x = document.querySelectorAll("p.example"); 

# HTML DOM Document 对象  runoob #
[https://www.runoob.com/jsref/dom-obj-document.html](https://www.runoob.com/jsref/dom-obj-document.html)