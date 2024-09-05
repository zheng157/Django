from django.contrib import admin
from django.urls import path
from ItemPool import views as itemPoolView #��Ӧ�õ�����ͼ
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getpapercontent/', itemPoolView.makePaperConent),
    path('getpaperindex/', itemPoolView.getPaperIndex),
    path('getpaper/', itemPoolView.getPaper),
    path('getdoc/', itemPoolView.getDoc),
]
