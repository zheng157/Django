from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from userdiy import views as diy_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('add/', diy_views.add_new,name='add_new'),
    path('change/', diy_views.change_user,name='change_user'),
]