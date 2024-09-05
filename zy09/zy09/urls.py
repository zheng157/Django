from django.urls import path
from zy09app import views


urlpatterns = [
    path('index/', views.index, name='blog_index'),
    path('add/', views.add, name='blog_add'),
    path('list/', views.list, name='blog_list'),
    path('detail/<blog_id>/', views.detail, name='blog_detail'),
    path('detele/<blog_id>/', views.detele, name='blog_detele'),
    path('edit/<blog_id>/', views.edit, name='blog_edit'),
]
