import re
"""
>>> d=re.match('^[0-9]{1,2}.','1.测试'.strip(' \r\n')) 正则表达式匹配
>>> d.group()   返回匹配的字符串
'1.'
>>> d.end()     返回字符串结束的位置
2
"""
from ItemPool.models import *
def imdata():
    f=open('d:/data.txt','r',encoding='UTF-8')
    okd=f.readlines()
    f.close()
    n=0
    x=1
    test=[]
    while n<len(okd):
        item={}
        d=re.match('^[0-9]{1,2}.',okd[n].strip(' \r\n'))    #匹配试题编号
        t=False
        if d:
            if n==0:
                t=True
            else:
                if n>5:
                    e=re.match('正确答案',okd[n-2].strip(' \r\n'))#匹配参考答案
                    if e:
                        t=True
        if t:                   #t为True时，表示题干开始
            q=okd[n][d.end():]
            q=q.strip(' \r\n')
            n=n+1
            while okd[n].strip(' \r\n')!='A':
                q=q+okd[n].rstrip(' \r\n')
                n=n+1
            
            item['question']=q
            n=n+1
            a=""
            while okd[n].strip(' \r\n')!='B':
                a=a+okd[n]
                n=n+1
            n=n+1
            b=""
            while okd[n].strip(' \r\n')!='C':
                b=b+okd[n]
                n=n+1
            n=n+1
            c=""
            while okd[n].strip(' \r\n')!='D':
                c=c+okd[n]
                n=n+1
            n=n+1
            d=""
            while not re.match('正确答案',okd[n].strip(' \r\n')):  #匹配参考答案，遇到参考答案行，则选项D结束
                d=d+okd[n]
                n=n+1
            item['option']={'A':a,'B':b,'C':c,'D':d}           
            an=okd[n].strip(' \r\n')
            an=an[len(an)-1:]
            item['answer']=an.rstrip(' \r\n')
            test.append(item)
            print(item)
        n=n+2
    it=itemType.objects.get(id=1)
    for a in test:
        n=testItem.objects.create(question=a['question'],options=a['option'],answer=a['answer'],type=it)        
    print('处理完毕') 
