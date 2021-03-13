from django.shortcuts import render

# Create your views here.
def Firstpage(response):
    context={'a':'a'}
    return render(response, 'index.html', context)