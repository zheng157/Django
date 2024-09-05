from django.db import models

class scores(models.Model):
    kh=models.CharField(max_length=8)
    xm=models.CharField(max_length=8)
    yw=models.SmallIntegerField()
    sx=models.SmallIntegerField()
    bj=models.CharField(max_length=8)
