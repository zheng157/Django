from django.urls import path
from . import views
from newuser import views as newuser_views
urlpatterns = [
    path('mdiy/', views.usePersonFormDIY),
    path('media/', views.usePersonFormDIY_Media),
    path('newfirst/', newuser_views.toAddNew),
    path('checkuid/', newuser_views.doCheckUid), 
    path('getpng/', newuser_views.createImg), 
    path('checkcode/', newuser_views.returnCheckCode), 
    path('addnew/', newuser_views.doAddNew), 
]
                                                          

