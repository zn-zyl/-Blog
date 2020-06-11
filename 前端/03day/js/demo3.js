//单行注释://
// window.open("https://www.baidu.com")

/*
多行注释
python
java
*/


//js的变量可以先申明后赋值
var name;
name = 'musen';
var age = 18;

var a = 19;
b = 22;
c = 66;
//控制台输出
console.log(name)
console.log(a)

//js中的条件语句
var c = 100
if (c < 50) {
    console.log(c)
} else if (c == 50) {
    console.log("sss")
} else {
    console.log("ss")
}

//js函数函数的定义
function myFunc(a, b) {
    //计算两个数相加的结果并调用
    var c = a + b
    // console.log(c)
    return c
}

//函数调用
var res = myFunc(1, 2)
console.log(res)

//json中的对象
var obj = {
    a: 1,
    b: 2,
    func01: function (aa, bb) {
        //对象的方法
        return aa * bb
    },
    func02: function () {
        var res = this.a + this.b
        return res
    }
}

var obj01 = new Object();

//while 循环
var i = 1
while (i <= 5) {
    i ++
    // alert(i)

}

//for循环
//形式一      遍历数组遍历出的是下标  遍历对象出来的是属性   for i in xx
var alist=[1,2,3,4]
for (i in alist){
    console.log(i)
    console.log(alist[i])
}

var obja={
    a:11,
    b:22,
    c:33,
    func02: function () {
        var res = this.a + this.b
        return res                          
}}
for (i in obja){
    console.log(i)
}

//形式2      for (语句1，语句2，语句3){}
//语句1：循环开始前执行 2是否执行循环体的条件 语句3 每轮循环体之后执行


for(var i=1;i<=5;i++){
    console.log(i);
}