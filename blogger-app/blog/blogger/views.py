from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blogger import models
from datetime import datetime

def home(request):
    
    if request.method=="POST":
        
        title=request.POST.get('title')
        body=request.POST.get('body')
        
        postblog = models.BlogPost(title=title, body=body,username=request.user, timestamp=datetime.now())
        postblog.save()

        return redirect('/')
        
    posts = models.BlogPost.objects.all()
    return render(request, 'base.html', {'posts':posts})

def loginuser(request):

    if request.method=="POST":
        
        username = request.POST.get('username')
        pword = request.POST.get('pass')
        
        logged = authenticate(username=username, password=pword)

        if logged is not None:
            login(request, logged)
            return redirect('/')
        else:
            return redirect('/loginuser')

    else:
        return render(request, 'loginuser.html')

def logoutuser(request):
    logout(request)

    return redirect('/')

def signup(request):
    if request.method=="POST":
        
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass')
        pass2=request.POST.get('repass')

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()
        messages.success(request, "Successfully Logged in")
        return redirect('./loginuser')

    else:
        return render(request, 'signup.html')

def comments(request):
    
    
    return render(request, 'comments.html')