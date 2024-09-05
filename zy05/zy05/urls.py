from django.contrib import admin
from django.urls import path
from ItemPool import views as itemPoolView #从应用导入视图
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getpapercontent/', itemPoolView.makePaperConent),
    path('getpaperindex/', itemPoolView.getPaperIndex),
    path('getpaper/', itemPoolView.getPaper),
    path('getdoc/', itemPoolView.getDoc),
]
