## 定义和用法 ##
forEach() 方法用于调用数组的每个元素，并将元素传递给回调函数。

注意: forEach() 对于空数组是不会执行回调函数的。

forEach() 方法用于调用数组的每个元素，并将元素传递给回调函数。

## 列出数组的每个元素： ##

    <button onclick="numbers.forEach(myFunction)">点我</button>
    <p id="demo"></p>
     
    <script>
    
	demoP = document.getElementById("demo");
    var numbers = [4, 9, 16, 25];
     
    function myFunction(item, index) {
    	demoP.innerHTML = demoP.innerHTML + "index[" + index + "]: " + item + "<br>"; 
    }
    </script>


forEach() 本身是不支持的 continue 与 break 语句的，我们可以通过 some 和 every 来实现。

使用 return 语句实现 continue 关键字的效果：

## continue 实现 ##

跳过3循环

    var arr = [1, 2, 3, 4, 5];
    
    arr.forEach(function (item) {

	    if (item === 3) {
	    	return;
	    }
	    console.log(item);
    });


## break 实现 ##

遇到3，退出循环

    var arr = [1, 2, 3, 4, 5];
    
    arr.every(function (item) {

		// every() 方法用于检测数组所有元素是否都符合指定条件

	    console.log(item);
	    return item !== 3;
    });