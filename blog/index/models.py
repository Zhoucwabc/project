from django.db import models

# Create your models here.
from user.models import User


class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name

    def Meta(self):
        db_table = 'type_name'


class Category(models.Model):
    cate_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cate_name

    def Meta(self):
        db_table = 'cate_name'


class Blog(models.Model):
    blog_title = models.CharField(max_length=20)
    blog_main = models.CharField(max_length=20)
    blog_time = models.DateTimeField()
    blog_read = models.IntegerField(default=0)
    blog_like = models.IntegerField(default=0)
    bloguser = models.ForeignKey(User,on_delete=models.CASCADE)
    blogtype = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_title

    def Meta(self):
        db_table = 'blog_title'


