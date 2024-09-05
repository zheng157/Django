from django.http import HttpResponse
def index(request):
    html='这是我的第一个Django网页！<br/><img src="/static/pic2.png">'
    return HttpResponse(html)