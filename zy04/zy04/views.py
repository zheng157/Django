from django.http import HttpResponse
from datetime import date
from .import models

def showData(request,urlData):
    d=date.today()
    s="URL路径中的数据: %s<br>当前日期: %s"%(urlData,d)
    return HttpResponse(s)

def showSomething(request):
    s='请求上传的数据:姓名=%s，年龄=%s' % (request.GET['name'],request.GET["age"])
    return HttpResponse(s)
from . import models

def useModels(request):
    uname=request.GET['name']
    uage=request.GET['age']
    models.user.objects.create(name=uname,age=uage)
    s= "默认数据库中的user表数据:<br><table><tr><td>id</td><td>name</td><td>age</td></tr>"
    for u in models.user.objects.all():
        s+="<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (u.id,u.name,u.age)
    return HttpResponse(s+'</table>')


from django.core.paginator import Paginator
def useModelsPaginator(request):
    objects=models.user.objects.all()
    pages=Paginator(objects,2)
    page_number = request.GET['page']
    page = pages.get_page(page_number)
    list=page.object_list
    s="数据分页显示<hr><table><tr><td>id</td><td>name</td><td>age</td></tr>"
    for u in list:
        s+="<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (u.id,u.name,u.age)
    s+="</table><hr/>"
    if(page.has_previous()):
        s+=' > <a href="/pages?page=%s">上一页<a/>' % page.previous_page_number()
        s+='当前页:%s/%s' % (page.number,pages.num_pages)
    if(page.has_next()):
        s+=' > <a href="/pages?page=%s">下一页<a/>' % page.previous_page_number()
    return HttpResponse(s)

