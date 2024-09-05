from django.http import HttpResponse
from django.shortcuts import render
import datetime
 
# ������������
def get_time(request):  
    # ��õ�ǰʱ��
    now = datetime.datetime.now()
    # ת��Ϊָ���ĸ�ʽ:
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    # render��������html�ļ�,{}������Ҫ����ģ��ĵı���
    return render(request, "dynamic_time.html", {"year": now.year,"month":now.month,"day":now.day,"hour":now.hour,"min":now.minute,"sec":now.second})