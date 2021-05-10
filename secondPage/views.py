from django.shortcuts import redirect, render
from .models import SensorData, UserSensor
from .forms import UserMapForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
# Create your views here.
@csrf_exempt
def second(request):
    if(request.method == 'POST'):
        data = request.POST
        method = request.POST.get("_method")
        if method == "delete":
            delItem = data.get('userValue')
            x = UserSensor.objects.get(pk = delItem)
            x.delete()
            return redirect("/second")
    if(request.user.is_authenticated):
        form = UserMapForm(request.POST or None, initial = {"Uid" : request.user.id})
        if(form.is_valid and request.POST  and request.method == 'POST'):
            form.save()
            print(form.cleaned_data)
            return redirect("/second")
        userD = UserSensor.objects.filter(Uid = request.user.id)
        context = {
            'user' : request.user,
            'sensorData' : SensorData.objects.all(),
            'SelectedSensor' : userD,
            'form' : form,
        }
        return render(request, 'secondP.html', context)
    
    else:
        return redirect("/login")

