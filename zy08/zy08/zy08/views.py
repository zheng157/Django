from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse


# Create your views here.

def home(request):
    # 主页面
    username = request.session.get('username', '未登录')
    return render(request, 'home.html', locals()) # locals方法，自动传参


def login_test(request):
    # 登陆
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            request.session['username'] = username
            request.session.set_expiry(0)  # 关闭浏览器就过期
            return redirect(reverse('ss_home'))
        return HttpResponse('请输入用户名')
    else:
        return render(request, 'login.html')

def logout_test(request):
    # 退出
    request.session.flush()
    return redirect(reverse('ss_home'))


from django.views import View
from .forms import RegisterForm
from .models import User_Form


class Register(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        form = RegisterForm(request.POST) # 获取表单提交上来的数据
        if form.is_valid(): # 如果数据符合规则
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password == password_repeat:  #　password = make_password(password) # 给密码加密，在数据库中就看不到真正的密码
                user = User_Form()
                user.username = username
                user.password = password
                user.email = email
                user.save()
                return redirect(reverse('ss_login'))
            return HttpResponse('注册失败')
        print(form.errors)
        return HttpResponse(form.errors)


from.forms import LoginForm


class LoginTest(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login_form.html', locals())

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User_Form.objects.filter(username=username, password=password)
            if user:        # if check_password(password.user[0].password):  # 还可以这样判断
                request.session['username'] = username
                return redirect(reverse('ss_home'))
            return redirect(reverse('ss_register'))
        print(form.errors)
        return HttpResponse(form.errors)