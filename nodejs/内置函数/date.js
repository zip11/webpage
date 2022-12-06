function RetnW() {
    
    //JS的数组
    var date=new Date(); 
    var day=date.getDay();
    var weeks=new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六");
    var week=weeks[day];
    return week

}



function retdw() {
    
    // day is ?
    var date=new Date(); 
    var day=date.getDay();

    if(day==2){
        console.log("day is 2" )
    }

}

// 获取 星期 几
console.log(RetnW());

// 获取 单独 日期
var date = new Date();
var year = date.getFullYear();
var month = date.getMonth()+1;

var day = date.getDate();
var hour = date.getHours();

var minute = date.getMinutes();
var second = date.getSeconds();

console.log(year+'年'+month+'月'+day+'日 '+hour+':'+minute+':'+second);

console.log(year+''+month+''+day+''+hour+''+minute+''+second);
