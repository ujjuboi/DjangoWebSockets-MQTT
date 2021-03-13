from django.shortcuts import render

# Create your views here.
def Graph(request):
    return render(request, 'graph.html')