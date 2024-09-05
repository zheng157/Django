from django.urls import path
from test065 import views as log_views

urlpatterns = [
    path('sendemail/', log_views.sendEmail),
]
