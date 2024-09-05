from django.http import HttpResponse
from django.shortcuts import render
import datetime
 
# 接收请求数据
def get_time(request):  
    # 获得当前时间
    now = datetime.datetime.now()
    # 转换为指定的格式:
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    # render用来加载html文件,{}里面是要传给模板的的变量
    return render(request, "dynamic_time.html", {"year": now.year,"month":now.month,"day":now.day,"hour":now.hour,"min":now.minute,"sec":now.second})