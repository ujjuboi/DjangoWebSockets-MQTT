from django.shortcuts import redirect, render
from .models import SensorData, UserSensor
from .forms import UserMapForm
from django.db.models import Q
# Create your views here.

def second(request):
    if(request.user.is_authenticated):
        form = UserMapForm(request.POST or None, initial = {"Uid" : request.user.id})
        if(form.is_valid and request.POST ):
            form.save()
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

