from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        nickname = request.POST['nickname']
        uemail = request.POST['uemail']
        print("uname:",uname,"upwd:",upwd,"nickname:",nickname,"uemail:",uemail)
        return redirect(reverse('login'))

def login_views(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        print('uname:',uname,'upwd',upwd)
        return redirect(reverse('index'))

def forget_views(request):
    if request.method == 'GET':
        return render(request, 'forget.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        print('uname:',uname,'upwd',upwd)
        return redirect(reverse('login'))
