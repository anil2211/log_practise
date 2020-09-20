from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponse
from .models import Login
# Create your views here.

def index(request):
    return render(request,"log.html")

def stu(request):
    obj=Login()
    obj.username=request.POST['username']
    obj.password=request.POST['password']
    obj.image=request.POST['image']

    obj.save()
    return redirect('/show')

def doLogin(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        data=Login.objects.get(username=username,password=password)
        request.session['usernameSession']=username
        return render(request,'home.html',{'username':username})
    except:
        return render(request,'log.html',{'loginError':'Invalid username or password'})


def show(request):
    list=Login.objects.all()
    return render(request,'show.html',{'list':list})

def delete(request, id):  
    list = Login.objects.get(id=id)  
    list.delete()  
    return redirect('/show') 