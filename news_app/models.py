from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth import get_user_model

class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    p1 = models.TextField(default="")
    p2 = models.TextField(default="", blank=True)
    p3 = models.TextField(default="", blank=True)
    sources = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title
