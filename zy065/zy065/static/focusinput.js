$(function () {
    $("input,textarea").focus(function () {
        $(this).addClass("inputfocus");         //��ý���ʱ����࣬�ı䱳����ɫ
    });
    $("input,textarea").blur(function () {
        $(this).removeClass("inputfocus");      //ʧȥ����ʱɾ���࣬�ظ�Ĭ�ϱ�����ɫ
    });
})