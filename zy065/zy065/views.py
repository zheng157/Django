
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.forms import ModelForm,ValidationError
from .models import person
from django.forms import formset_factory
from django import forms
from django.shortcuts import render
from datetime import datetime

def validate_age(value):
  if int(value) < 20:
      raise ValidationError('年龄不能小于20！',code='min_value')
  elif int(value) > 50:
      raise ValidationError('年龄不能大于50！',code='max_value')

class personFormDIY(ModelForm):
    #重定义age字段
    age=forms.CharField(validators=[validate_age],label='年龄',\
                        widget = forms.NumberInput(),\
                        help_text = '年龄为[20,50]以内的整数')
    class Meta:
        model = person              #指定模型
        fields = ['name', 'age']    #指定字段
        labels = { 'name': '姓名',}   #设置字段渲染后的<label>内容
        help_texts = {'name':'姓名为中英文字符串',}#设置字段帮助文本
        widgets = {'name': forms.Textarea(attrs={'cols': 30, 'rows': 2}),}

def usePersonFormDIY(request):    
    if request.method == 'POST':  
        mform = personFormDIY(request.POST)
        if mform.is_valid():
            ps=person.objects.filter(name=request.POST['name'])
            if ps.count()==0:
                mform.save()
                msg='数据已保存！'
            else:
                msg='数据库已存在相同姓名的数据，请勿重复提交！'     
        else:msg='表单数据有错'
    else:
        mform = personFormDIY()
        msg="请输入数据添加新记录"
    return render(request, 'temmodelformdiy.html', {'mform': mform,'msg':msg})

class personFormDIY_Media(ModelForm):
    #重定义age字段
    age=forms.CharField(validators=[validate_age],label='年龄',\
                        widget = forms.NumberInput(),\
                        help_text = '年龄为[20,50]以内的整数')
    class Meta:
        model = person              #指定模型
        fields = ['name', 'age']    #指定字段
        labels = { 'name': '姓名',}   #设置字段渲染后的<label>内容
        help_texts = {'name':'姓名为中英文字符串',}#设置字段帮助文本
        widgets = {'name': forms.Textarea(attrs={'cols': 30, 'rows': 2}),}
    class Media:
        css={'all': ('/static/diyform.css',)}
        js = ('/static/focusinput.js',)

def usePersonFormDIY_Media(request):    
    if request.method == 'POST':  
        mform = personFormDIY_Media(request.POST)
        if mform.is_valid():
            ps=person.objects.filter(name=request.POST['name'])
            if ps.count()==0:
                mform.save()
                msg='数据已保存！'
            else:
                msg='数据库已存在相同姓名的数据，请勿重复提交！'     
        else:msg='表单数据有错'
    else:
        mform = personFormDIY_Media()
        msg="请输入数据添加新记录"
    return render(request, 'temmedia.html', {'mform': mform,'msg':msg})
