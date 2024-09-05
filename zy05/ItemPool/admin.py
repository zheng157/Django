from django.contrib import admin
#替换站点默认标题
admin.site.site_title="Python在线题库后台管理"  #定义站点标题（显示在浏览器标题栏）
admin.site.site_header="Python在线题库"         #定义站点页面顶部标题

from .models import *
admin.site.register(paperTemplate) #按默认方式注册模型

@admin.register(itemType)       #用下面的自定义类注册试题类型模型
class itemTypeAdmin(admin.ModelAdmin):
    list_display=['id','name']  #设置在模型数据浏览页面中显示的字段
    list_editable=['name']      #允许在模型数据浏览页面中修改数据

@admin.register(testItem)     #注册试题模型
class testItemAdmin(admin.ModelAdmin):
    list_display=['id','type','question','options','item_pic','answer']
    list_filter=['type__name']#设置过滤器字段
    ordering=['type','id']#允许对type和ID字段排序
    search_fields = ['question']#设置搜索字段，在页面中显示搜索框
    add_form_template='change_testItem.html'    #设置添加数据表单模板
    change_form_template='change_testItem.html'#设置修改数据表单模板
    fieldsets = (#定义添加和修改页面中字段及其先后顺序
        (None, {
            'fields': ('type','question','options','picture','answer')
        }), )

@admin.register(paperContent)     #注册试卷内容模型
class paperContentAdmin(admin.ModelAdmin):
    list_display=['id','name','content','template']
    ordering=['id','name','template']
    add_form_template='paperContent.html'
    change_form_template='paperContent.html'
    list_filter=['name']#设置过滤器字段
    search_fields = ['template']#设置搜索字段，在页面中显示搜索框
    fieldsets = (
        (None, {
            'fields': ('template','name','content')
        }), )


