from django.conf.urls import url
from .views import *
urlpatterns=[
    url(r'^$',index_views,name='index'),
    url(r'^info/$',info_views,name='info'),
    url(r'^list/$',list_views,name='list'),
]
