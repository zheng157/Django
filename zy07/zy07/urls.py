
from django.urls import path
from . import views
from django.contrib import admin
#from django.conf.urls import url
from . import dynamic_time

urlpatterns = [
    path('time', views.getTime),#��̬ʱ��
    path('admin/', admin.site.urls),
    path(r'^dynamic_time/$', dynamic_time.get_time),#��̬ʱ��
]


