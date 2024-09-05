from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return 'Blog<title=%s, content=%s>'%(
            self.title, self.content
        )