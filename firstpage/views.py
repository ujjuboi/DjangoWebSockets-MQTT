from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm, UsersRegisterForm

# Create your views here.
def Firstpage(request): 
    context={'a':'a'}
    return render(request, 'index.html', context)

def login_view(request):
	form = UsersLoginForm(request.POST or None)
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

def register_view(request):
	form = UsersRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")	
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		return redirect("/")
	return render(request, "forms.html", {
		"title" : "Register",
		"form" : form,
	})
 