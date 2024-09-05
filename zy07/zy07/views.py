from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
def getTime(request):
    time=datetime.today()
    t=get_template('mytemplate.html')
    html=t.render({'time':time})
    return HttpResponse(html)
