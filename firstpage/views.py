from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UsersLoginForm, UsersRegisterForm
from .models import UserGroup
from django.utils.crypto import get_random_string
from django.db.utils import IntegrityError
from sqlite3 import IntegrityError
# Create your views here.
def Firstpage(request): 
    context={'a':'a'}
    return render(request, 'index.html', context)

def login_view(request):
    form = UsersLoginForm(request.POST or None)
    if request.user.is_authenticated == True:
        return redirect('/second')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        login(request, user)
        # if request.user.is_authenticated:
        # 		print(request.user.id)
        # 		context={'user' : request.user}
        # 		return render(request,'secondP.html', context)
        # else:
        # 	return redirect("/")
        return redirect('/second')
    return render(request, "forms.html", {
        "form" : form,
        "title" : "Login",
    })

def logout_view(request):
    logout(request)
    return redirect("/")

def register_view(request):
    form = UsersRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")	
        user.set_password(password)
        user.save()
        createUserGroup(user)
        new_user = authenticate(username = user.username, password = password)
        login(request, new_user)
        return redirect("/")
    return render(request, "forms.html", {
        "title" : "Register",
        "form" : form,
    })
 
def createUserGroup(user):
    y = 1
    while(y):
        try:
            x = UserGroup(user = user, group = get_random_string(length=8,allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
            x.save()
            y = 0
        except IntegrityError:
            y = 1

