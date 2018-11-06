from django.contrib import admin
from .models import *

# Register your models here.

class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cate_name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_main','blog_time','blog_read','blog_like','bloguser','blogtype','category')
    list_editable = ('blog_main','blog_time','blog_read','blog_like','bloguser','blogtype','category')



admin.site.register(BlogType,BlogTypeAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
