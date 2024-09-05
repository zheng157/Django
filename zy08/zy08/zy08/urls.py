from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='ss_home'),
    path('login/', views.LoginTest.as_view(), name='ss_login'),
    path('login_test/', views.login_test, name='login_test'),
    path('logout_test/', views.logout_test, name='ss_logout'),
    path('register/', views.Register.as_view(), name='ss_register'),
]