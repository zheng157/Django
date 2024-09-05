from django.urls import path
from .import views


urlpatterns = [
    path('test<urlData>',views.showData),
    path('get/',views.showSomething),
    path('model',views.useModels),
    path('pages',views.useModelsPaginator),
]
