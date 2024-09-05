from django.contrib import admin
from django.urls import path
from first import views
urlpatterns = [
    path('first/', views.index),
    path('admin/', admin.site.urls),
]