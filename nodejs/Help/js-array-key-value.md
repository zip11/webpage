## 使用 JavaScript Object 来存储键值数组 ##
## 使用 JavaScript Map 来存储键值数组 ##

JavaScript 中的数组是存储不同元素的单个变量。我们可以需要它们来存储一个元素列表，每个元素都有一个索引，通过它来访问它们。JavaScript 有不同的方法来存储一个键值数组。

使用 JavaScript Object 来存储键值数组
JavaScript 中的 Object 是一个有属性的实体，每个属性都有值，所以键值术语可以在它身上发挥作用。

举个例子

    let obj1 = { id: 1, name: 'Mark', age: 30, country: "USA" };
    obj1.city = "New York";
    obj1['job'] = "software developer";
    
    console.log(obj1);
输出：

    {
    age: 30
    city: "New York"
    country: "USA"
    id: 1
    job: "software developer"
    name: "Mark"
    }
我们可以通过它进行循环。

    let obj1 = { id: 1, name: 'Mark', age: 30, country: "USA" };
    obj1.city = "New York";
    obj1['job'] = "software developer";
    
    for (let key in obj1) {
      console.log(key + " => " + obj1[key]);
    }
输出：

    id => 1
    name => Mark
    age => 30
    country => USA
    city => New York
    job => software developer
如果我们有一个数组，我们可以在数组中逐个循环，将每个元素的索引中的键值和 Object 中对应的值相加。

    let arr1 = ["delfstack", "Computer", "Science"]; 
    
    let obj1 = {}; 
    
    for(let i = 0; i < arr1.length; i++){ 
      obj1[i] = arr1[i]; 
    } 
    
    for (let key of Object.keys(obj1)) { 
      console.log(key + " => " + obj1[key] ) 
    } 
输出：
    
    0 => delfstack
    1 => Computer
    2 => Science
使用 JavaScript Map 来存储键值数组
Map 就像 Object 一样。它是一个带键数据项的列表。不同的是，Map 允许任何类型的键。

## JavaScript Map 的语法 ##
    let map = new Map();

存储键 => 值。
    map.set('name', 'mark');
 
Java Map 示例
    let arr1 = ["delfstack", "Computer", "Science"]; 
    
    let map = new Map(); 
    
    for(let i = 0; i < arr1.length; i++){ 
      map.set(i, arr1[i]); 
    } 
    
    for (let key of map.keys()) { 
      console.log(key + " => " + map.get(key) ) 
    } 
输出：
    
    0 => delfstack
    1 => Computer
    2 => Science