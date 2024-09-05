$(function () {
    $("input,textarea").focus(function () {
        $(this).addClass("inputfocus");         //获得焦点时添加类，改变背景颜色
    });
    $("input,textarea").blur(function () {
        $(this).removeClass("inputfocus");      //失去焦点时删除类，回复默认背景颜色
    });
})