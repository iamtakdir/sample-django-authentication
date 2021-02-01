from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm , SignForm
from django.contrib.auth.models import User



def index(request):
    
    return render (request,'users/index.html')


def user_login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("You are fuking Authenticated")
                    
                else:
                    return HttpResponse("You are fucked up :3 ")
            else:
                return HttpResponse(" No one gives a fuck to you ")
                
    else:
        form = LoginForm()
    return render (request,'users/loginuser.html',{'form':form})
    

def user_signup(request):

    if request.method == 'POST':
        form = SignForm(request.POST)

        if form.is_valid():

            

            cd = form.cleaned_data

            username = cd['username']
            password = cd['password']
            email = cd['email']
            
            user = User.objects.create_user(username, email, password)

            user.save()

            return redirect(user_login)

    else:
        form = SignForm()


    return render (request, 'users/signup.html', {'form':form})

   