JavaScript遍历对象的几种方法

## for 循环 ##

    for(var i = 0; i < name.length; i++) {
      console.log(name[i]);
    }

## 一、for...in ##

for...in 用于以任意顺序遍历对象所有的可枚举属性（包括对象自身的和继承的可枚举属性，不含 Symbol 属性）。

    let obj = {
	    name: 'Scarlett',
	    age: 37,
	    [Symbol()]: 'Johansson'
    }

    for (let key in obj) {
    	console.log(key) // name age
    }


## 二、for...of ##

for...of 是 ES6 新增的遍历方式，它为不同的数据结构提供了统一的遍历机制。任何数据结构只要实现了 Iterator 接口的，都可以被遍历。关于 Iterator 接口可以参考 这里

for...of 循环可以使用的范围包括 Array、Set 和 Map 结构、类数组对象（比如arguments 对象、DOM NodeList 对象）、字符串等。

### 1.类数组对象 ###

以下是 for...of 循环字符串、arguments 对象、DOM 元素集合的例子：

    // 字符串
    let str = "hello";

    for (let s of str) {
    	
		console.log(s); 
		// h e l l o
    
	}