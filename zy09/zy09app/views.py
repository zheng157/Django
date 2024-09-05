from django.shortcuts import render, redirect, reverse
from .models import Blog
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'demo_index.html')

def add(request):
    if request.method == 'GET':
        return render(request, 'demo_add.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Blog(title=title, content=content).save()
        return redirect(reverse('blog_add'))
    else:
        return HttpResponse('操作有误')


def list(request):
    lis = Blog.objects.all()
    return render(request, 'demo_list.html', context={
        'blog_list': lis
    })

def detail(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    if blog:
        return render(request, 'demo_detail.html', context={
            'blog': blog
        })
    return HttpResponse('输入有误')

def detele(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)
    if blog:
        blog.delete()
        return redirect(reverse('blog_list'))
    else:
        return HttpResponse('操作有误')


def edit(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    if blog:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            Blog.objects.filter(id=blog_id).update(title=title, content=content)
            return redirect(reverse('blog_add'))
        return render(request,'demo_detail.html', context={
            'blog': blog
        })
    return HttpResponse('操作异常')