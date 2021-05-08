from django.shortcuts import redirect, render
from .models import SensorData, UserSensor
from .forms import UserMapForm
# Create your views here.

def second(request):
    if(request.user.is_authenticated):
        # userD = UserSensor.objects.filter(Uid = request.user.id)
        
        form = UserMapForm(request.POST or None, initial = {"Uid" : request.user.id})
        if(form.is_valid and request.POST ):
            form.save()
        context = {
            'user' : request.user,
            'sensorData' : SensorData.objects.all(),
            # 'userSensor' : userD,
            'form' : form,
        }
        return render(request, 'secondP.html', context)
    
    else:
        return redirect("/login")

