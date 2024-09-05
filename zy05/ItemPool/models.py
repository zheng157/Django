from django.db import models
from django.utils.html import format_html
class itemType(models.Model): #试题类型模型
    name=models.CharField(max_length=10,verbose_name='试题类型名称') 
    #itemType和testItem是一对多关系，在testItem对象得添加和修改页面中，
    #默认显示关联对象“itemType object(1)”等，为模型定义__str__方法，
    #可使关联对象显示为__str__方法方法返回值。
    def __str__(self):          
       return self.name
    class Meta:
        #默认情况下itemType在Admin站点中的单数名称为Item type，复数名称为Item types
        verbose_name="试题类型" #设置模型在Admin站点中显示的单数名称
        verbose_name_plural = "试题类型"#设置模型在Admin站点中显示的复数名称

class testItem(models.Model): #试题模型
    question=models.TextField(max_length=600,verbose_name='试题题干') 
    options=models.TextField(max_length=600,verbose_name='试题选项',null=True,blank=True)
    #图片保存到MEDIA_ROOT+'/pics'目录，upload_to只能是相对路径
    picture=models.ImageField(upload_to='picssss',verbose_name='试题图片',null=True,blank=True) 
    answer=models.TextField(max_length=1000,verbose_name='参考答案')
    type=models.ForeignKey(itemType,on_delete=models.CASCADE,\
                                        verbose_name='试题类型') #外键，关联试题类型
    def item_pic(self):
        if self.picture:
            return format_html(    #在Admin站点中正确显示图片
                 '<img src="{}" width="100px"/>','/static/'+self.picture.url)
        else:
            return "无图片"
    item_pic.short_description = '试题图片'
    class Meta:
        verbose_name="试题"
        verbose_name_plural = "试题"

class paperTemplate(models.Model): #试卷模板模型
    name=models.CharField(max_length=20,verbose_name='试卷模板名称') 
    date=models.DateTimeField(verbose_name='制卷时间') 
    typeOneCount=models.PositiveSmallIntegerField(default=40,verbose_name='单项选择题数量') 
    typeOneScore=models.DecimalField(default=1,max_digits=3,
                                     decimal_places=1,verbose_name='单项选择题分值')  
    typeTwoCount=models.PositiveSmallIntegerField(default=3,verbose_name='基本操作题数量')
    typeTwoScore=models.DecimalField(default=5,max_digits=3,\
        decimal_places=1,verbose_name='基本操作题分值')
    typeThreeCount=models.PositiveSmallIntegerField(default=2,verbose_name='简单应用题数量')
    typeThreeScore=models.DecimalField(default=12.5,max_digits=3,\
        decimal_places=1,verbose_name='简单应用题分值')
    typeFourCount=models.PositiveSmallIntegerField(default=1,verbose_name='综合应用题数量')
    typeFourScore=models.DecimalField(default=20,max_digits=3,\
        decimal_places=1,verbose_name='综合应用题分值') 
    def __str__(self):  #定义该方法，在Admin站点中引用模型对象时显示方法返回值        
        return self.name
    class Meta:
        verbose_name="试题模板"
        verbose_name_plural = "试题模板"
class paperContent(models.Model): #试卷内容模型，保存根据试卷选项生成的试卷                     				
    name=models.CharField(max_length=20,verbose_name='试卷名称')
    content=models.TextField(max_length=400,verbose_name='试题ID列表')
    template=models.ForeignKey(paperTemplate,\
        on_delete=models.CASCADE,verbose_name='试卷模板')#外键，关联试卷模板	
    def __str__(self):  #定义该方法，在Admin站点中引用模型对象时显示方法返回值        
        return self.name
    class Meta:
        verbose_name="试题内容"
        verbose_name_plural = "试题内容"