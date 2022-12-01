# javaScript正则表达式提取字符串中字母、数字、中文 && 字符串替换#

[https://blog.csdn.net/qq_45458749/article/details/124596123](https://blog.csdn.net/qq_45458749/article/details/124596123)

mozilla

[https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Regular_Expressions)

- g

如果正则表达式带g标志, replace()方法会替换字符串中的所有匹配项; 否则, 它只替换第一个匹配项。

- []

方括号用于查找某个范围内的字符：[0-9]

- \u

\uxxxx	查找以十六进制数 xxxx 规定的 Unicode 字符。

- ^
匹配输入的开始


----------


提取数字....

    value.replace(/[^\d]/g,'')

提取中文....

    value.replace(/[^\u4E00-\u9FA5]/g,'')

提取英文.....

    value.replace(/[^a-zA-Z]/g,'')



## 字符串替换（全部替换 && 仅替换第一个匹配的） ##

//将字母i全部替换成5



    var txt = "sjfisjfisdjfijsidfjioalfjewofjjgs";
    alert(txt .replace(/i/g,"5"));



//只将第一个字母i替换成5



    var txt = "sjfisjfisdjfijsidfjioalfjewofjjgs";
    alert(txt .replace("i","5"));
    
