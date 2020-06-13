// window.onload = function () {
//
// };


$(function () {
    // 页面加载完毕之后才会执行
    var b1 = $("#box1");
    console.log(b1.text());

    //
    var musen = $('#musen');

    //  console.log(musen.text());
    // // 查找父级标签
    // console.log(musen.parent());
    // // 找上一个兄弟节点：prev
    // console.log(musen.prev().text());
    // // next:下一个兄弟节点
    // console.log(musen.next().text());
    // // 查找子元素
    // console.log(musen.children().text());
    // 找前面所有的兄弟节点
    //  console.log(musen.prevAll());
    // 找后面所有的兄弟节点
    console.log(musen.nextAll());

});



