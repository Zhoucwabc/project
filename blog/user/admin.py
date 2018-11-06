from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('nickname','uname','upwd','uemail','isAuthor','isActive')
    list_editable = ('uname','upwd','uemail','isAuthor','isActive')


admin.site.register(User,UserAdmin)
