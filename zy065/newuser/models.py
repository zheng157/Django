from django.db import models
class userinfo(models.Model):
    uid=models.CharField (max_length=10,verbose_name='用户名',\
                        help_text='用户名由英文字母、数字等字符组成')
    password=models.CharField(max_length=6,verbose_name='密码',\
                        help_text='登录密码由6-8位字符组成')
    email=models.CharField(max_length=30,verbose_name='Email',\
                        help_text='有效电子邮件地址')
