# javascript 获取上级、同级和下级元素 #


----------


## 1. javascript 获取上级元素（父节点） ##​​​​​​

### 1) parentNode 获取上级元素 ###

    //当前元素直接父元素，parentNode 是 W3C 标准
    var parent = document.getElementById('test').parentNode;

### 2) parentElement 获取上级元素 ###

    //当前元素直接父元素，parentElement 是 IE 的标准
    var paernt = document.getElementById('test').parentElement;

### 3) offsetParent 获所有上级元素（牛逼） ###

    //offset(偏移量) 与这位置有关的上下级
    var parents = document.getElementById('test').offsetParent;


----------


## 2. javascript 获取同级元素（兄弟节点） ##

### 1) previousElementSibling，nextElementSibling：直接匹配节点；previousSibling，nextSibling：会匹配空格 ###

    //不匹配空格、换行，直接匹配元素
    var pre_brother  = document.getElementById('test').previousElementSibling;
    var next_brother = document.getElementById('test').nextElementSibling;
    
    //匹配空格、换行
    var pre_brother  = document.getElementById('test').previousSibling;
    var next_brother = document.getElementById('test').nextSibling;



----------


## 3. javascript 获取下级元素（子节点）##

### 1) 首选 children ###

    //children 返回数组
    var Chlid = document.getElementById('test').children[0]
    

### 2) DOM 方式 getElementByTagName ###

    //getElementByTagName 返回数组，需按数组形式访问
    
    var child = document.getElementById('test').getElementsByTagName('p');


### 3) childNodes 方式 ###

    //childNodes 返回子节点的集合（数组格式）注意：换行、空格也当作节点信息
    var child = document.getElementById('test').childNodes;


### 4) 获取第一个子节点或最后一个子节点（firstChild，firstElementChild，lastChild，lastElementChild） ###

    //firstChild,lastChild 空格、换行也会当成字节点，所以可能会现 undefined

    var firstchild = document.getElementById('test').firstChild;
    var lastchild = document.getElementById('test').lastChild;
    
    //firstElementChild,lastElementChild 不匹配空格、换行

    var firstchild = document.getElementById('test').firstElementChild;
    var lastchild = document.getElementById('test').lastElementChild;


总结：Element 指的是元素，带这个就是直接匹配元素，不匹配空可行和换行。

注意：如果返回是数组 Elements