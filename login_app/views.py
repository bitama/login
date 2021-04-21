from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,"index.html")

def register_user(request):
    errors=User.objects.validator(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v)
        return redirect("/")
    else:
        pw_hash=bcrypt.hashpw(request.POST["password"].encode(),bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            password=pw_hash
        )
        messages.info(request,"You have successfully created account please log in!!! ")
    
    return redirect("/")

def user_login(request):
    try:
        user=User.objects.get(email=request.POST["email"])
    except:
        messages.error(request,"Incorrect email address or password")
        redirect("/")
    if bcrypt.checkpw(request.POST["password"].encode(),user.password.encode()):
        request.session["id"] = user.id
        request.session["first_name"] = user.first_name
        request.session["last_name"] = user.last_name
        request.session["email"] = user.email
        return redirect("/user/success")
    messages.error(request,"Invalid email address or password")
    return redirect("/")
def user_success(request):
    if"id" not in request.session:
        messages.error(request,"Try log in again")
        return redirect("/")
        
    return render(request,"success.html")

def user_logout(request):
    if "id" in request.session:
        del request.session["id"]
    if "first_name" in request.session:
        del request.session["first_name"]
    if "last_name"in request.session:
        del request.session["last_name"]
    if "email" in request.session:
        del request.session["email"]
    request.session.clear()
    return redirect("/")
        
    
