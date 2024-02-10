
from django.shortcuts import render,redirect
from django.contrib.auth.models import User #User Model
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    # if request.user.is_authenticated:
    #     redirect("all_foods")
    if request.method=='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get('last_name')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_exists=False
        
        # if User.objects.filter(email=email).exists():
        #    messages.error(request,"E-mail is already Taken,Try with new one")
        #    user_exists=True
        # if user_exists:
        #     return render(request,'user/signup.html')
        user=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=email,
            password=password,
            date_joined=dob
        )
        user.save()
        messages.success(request,"Account Created Successfully Login To Continue")
    return render(request,'user/signup.html')

def signin(request):
    # if request.user.is_authenticated:
    #     redirect("all_foods")
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=email,password=password)
        if user is None:
            messages.error(request,"Invalid Username or Password")
            return render(request,'user/signin.html')
        else:
            login(request,user)
            return redirect("index")
        
    return render(request,'user/signin.html')

def signout(request):
    logout(request)
    return render(request,'user/signin.html')