from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=20)
    uemail = models.EmailField(null=True)
    isActive = models.BooleanField(default=True)
