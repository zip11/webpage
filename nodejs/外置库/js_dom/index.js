const fs = require('fs');
const jsdom = require("jsdom");
const jquery = require('jquery');
// dom 元素 选择器

// 获取html dom元素 文本， jsdom是html dom 解析器

const { JSDOM } = jsdom;

var dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p><input type="hidden" name="formhash" value="1234567890" />`);;


var window = dom.window; 
// 获取 window 对象

var document = dom.window.document; 
// 获取 document 对象

var $ = jquery(window); 
// 实例化jquery需要传入window对象

// body ----s
//console.log(document.body.innerHTML);
// body html
//console.log($("body").html());

// input 获取 value
let mhh = $("input[name=\"formhash\"]").val()
console.log("mhash:"+mhh);

// 插入p 标签 ---s
// $('body').append('<p>我勒个去！</p>');

// console.log(document.documentElement.outerHTML); 
// 获取整个html代码----s

// dom.serialize() 比 document.documentElement.outerHTML 多了DOCTYPE
// console.log(dom.serialize());
