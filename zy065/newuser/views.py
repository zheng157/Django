from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from random import randint,choice
from PIL import Image,ImageDraw,ImageFont
from django.http import FileResponse
from .models import userinfo

def toAddNew(request):    
    return render(request,'newuser.html')

def doCheckUid(request):    
    ps=userinfo.objects.filter(uid=request.GET['uid'])
    if ps.count()==0:
        msg='ID可用'
    else:
        msg='ID已占用'   
    return HttpResponse(msg, content_type="text/text;charset=utf-8")
def getRandomChar():        #获取随机字符
    num =str(randint(0,9))       	#获得随机数字
    lower=chr(randint(97,122))		#获得随机小写字母
    upper=chr(randint(65,90))		#获得随机大写字母
    char=choice([num,lower,upper])	#选择要使用的随机字符
    return char

def createImg(request):    #创建验证码图片返回
    img=Image.new(mode="RGB",size=(160,30),color=(100,100,100))    #创建图片
    draw=ImageDraw.Draw(img)    #获取图片画笔，用于描绘字
    #设置字体，字体文件在项目同名子文件夹中    
    font=ImageFont.truetype(font="arial.ttf",size=24) 
    code=''
    for i in range(5):             
        c=getRandomChar()                   #获得随机字符
        draw.text((10+30*i,2),text=c,fill=(255,255,255),font=font)#根据坐标填充文字
        code+=c                             #记录验证码字符
    request.session['randomcode']=code      #将验证码存入session
    f=open("temp.png",'wb')
    img.save(f, format="png")
    f.close()
    return FileResponse(open("temp.png",'rb'))

def returnCheckCode(request):   
    return HttpResponse(request.session['randomcode'], content_type="text/text;charset=utf-8")


def doAddNew(request): 
    try:
        nuid = request.GET['uid']
        pwd = request.GET['pwd']
        nemail = request.GET['email']
        user=userinfo(uid=nuid,password=pwd,email=nemail)
        user.save()
        msg="已成功完成注册！"
        return HttpResponse(msg, content_type="text/text;charset=utf-8")
    except Exception as e:
        msg="意外出错：%s" % e
        return HttpResponse(msg, content_type="text/text;charset=utf-8")