from django.contrib import admin
from .models import myUser
admin.site.register(myUser)     #在Admin站点中注册模型