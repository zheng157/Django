from .models import myUser
from django.forms import ModelForm
class myUserForm(ModelForm):    #定义模型表单，用于处理myUser模型
    class Meta:
        model = myUser 
        fields = ['username', 'password','email','qq','phone']
        labels = {'username':'用户名', 'password':'密码','email':'Email'}#其他字段用默认labe


from django.forms.utils import ErrorList
class myErrorList(ErrorList):#自定义错误列表格式
    def __str__(self):
        return self.todivs()
    def todivs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' \
            % ''.join(['<div class="error">%s</div>' % e for e in self])


from django.shortcuts import render,redirect
from django.urls import reverse
def add_new(request): #处理添加新用户
    msg=''
    if request.method == 'POST':      		
        #在用户提交新用户数据时，用数据创建模型表单
        mform = myUserForm(request.POST,auto_id=False,error_class=myErrorList)
        if mform.is_valid():
            #在表单通过验证时执行数据处理
            user_name=mform.cleaned_data['username']
            password=mform.cleaned_data['password']
            u=myUser.objects.filter(username=user_name)	#用表单数据查询
            mform.save()				#将数据存入数据库
            #保存模型表单时，密码已明文的方式存入password字段，应通过set_password()方法设置密码
            u=myUser.objects.get(username=user_name)	#用表单数据查询
            u.set_password(password)  #正确处理密码字段
            u.save()                    #保存对密码的修改
            msg='数据已保存！'
        else:
            msg='数据有错，请修改后重新提交！'
    else:
        mform = myUserForm()				#创建空白表单
        msg='请输入数据添加注册新用户！'
    title='新用户注册，<a href="%s">登录</a>'%reverse('login')
    return render(request, 'edit_user.html', {'form': mform,'msg':msg,'title':title})


from django.contrib.auth.decorators import login_required
@login_required           #必须登录后才能修改个人数据
def change_user(request): #处理修改用户数据
    if request.method == 'POST':      		
        #提交表单时采用POST方法，用提交的数据修改当前用户
        mform = myUserForm(request.POST,auto_id=False,error_class=myErrorList)#创建表单        
        data_ok=mform.is_valid()    #执行表单验证，检查数据是否正确
        user_name=request.POST.get('username')  #获得提交的用户名        
        if not data_ok:
            #在没有修改用户名时，模型表单会报错，认为已存在相同的用户名
            #此时也应使用提交的数据修改用户，下面的语句用于检测这种情况
            error_msg='username already exists'
            username_error='%s'%mform.errors.get('username')
            if username_error.find(error_msg)>-1 and user_name==request.user.username:
                name_ok= True   #在未修改用户名时，忽略表单报告的用户名重复错误
            else:name_ok= False
        if data_ok or (name_ok and not data_ok):#数据通过校验时，用其修改当前用户
            u=myUser.objects.get(username=request.user.username)	#获得要修改的模型对象
            #本例中将修改和未修改用户名统一处理，所以在此更改了用户名
            u.username=user_name
            u.set_password(request.POST.get('password'))   #注意密码字段的修改方式
            u.email=request.POST.get('email')
            u.qq=request.POST.get('qq')
            u.phone=request.POST.get('phone')         
            u.save()                            #将模型对象数据写入数据库
            return redirect(reverse('login'))   #完成数据修改后，重定向到登录页面
        else:msg='数据有错，请修改后重新提交！'
    else:
        #请求方法不是POST，说明是通过URL请求，
        #此时用request中的已登录用户数据创建表单
        username=request.user.username
        email=request.user.email
        qq=request.user.qq
        phone=request.user.phone
        data={'username':username, 'password':'','email':email,'qq':qq,'phone':phone}
        mform = myUserForm(data,auto_id=False,error_class=myErrorList)#创建表单
        mform.errors.clear()    #表单会报告已存在同名用户错误，所以在此清楚错误信息
        msg='修改当前用户数据'
    title='修改用户数据，当前用户名：%s，<a href="%s">登录</a>'\
                          %(request.user.username,reverse('login'))
    return render(request, 'edit_user.html', {'form': mform,'msg':msg,'title':title})