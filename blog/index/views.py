from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_views(request):
    return render(request,'index.html')

def info_views(request):
    return render(request,'info.html')

def list_views(request):
    return render(request,'list.html')
