from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re
def validate_qq(value):#判断QQ号是否为[5,11]位数字
    s=re.match(r"^[1-9]\d{4,10}",value)
    if not( s and s.end()==len(value) and len(value)>4):
        raise ValidationError('QQ号不正确：%s' % value)
def validate_phone(value):#判断手机号是否正确
    s=re.match(r"1[3458]\d{9}",value)
    if not( s and s.end()==len(value) and len(value)==11):
        raise ValidationError('手机号不正确：%s' % value)
class myUser(AbstractUser):
    qq=models.CharField(max_length=11,verbose_name='QQ号',validators=[validate_qq])
    phone=models.CharField(max_length=11,verbose_name='手机号',validators=[validate_phone])