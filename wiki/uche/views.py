from turtle import title
from winreg import QueryValue
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def  home(request):
    return render (request, 'uche/home.html',{})

def user_login(request):
    context ={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))

        else:
            context["error"] = "Enter valid username or password !!"
            return  render(request, "uche/login.html", context)  


        
    else:
        return render(request, "uche/login.html", context)
    

def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "uche/success.html", context)


def user_logout(request):
    if request.method =="POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))


def search(request):
    q=request.GET['q']
    allposts= User.objects.filter(title__icontains=q)
    output={'allposts': allposts}
    return render(render,'uche/search.html', output )      
    