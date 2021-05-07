from django.shortcuts import redirect, render

# Create your views here.

def second(request):
    if(request.user.is_authenticated):
        context = {
            'user' : request.user
        }
        return render(request, 'secondP.html', context)
    
    else:
        return redirect("/login")