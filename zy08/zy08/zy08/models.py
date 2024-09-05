from django.db import models

# Create your models here.
class User_Form(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)