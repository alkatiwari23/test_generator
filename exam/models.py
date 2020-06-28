from django.db import models
from django.urls import reverse
# Create your models here.
class Questions(models.Model):
    ques=models.CharField(max_length=100)
    opt1=models.CharField(max_length=20)
    opt2 = models.CharField(max_length=20)
    opt3 = models.CharField(max_length=20)
    opt4 = models.CharField(max_length=20)
    ans = models.CharField(max_length=20)
    tag=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.ques

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])