from django.shortcuts import redirect, render
from .models import SensorData, UserSensor
# Create your views here.

def second(request):
    if(request.user.is_authenticated):
        userD = UserSensor.objects.filter(Uid = request.user.id)
        context = {
            'user' : request.user,
            'sensorData' : SensorData.objects.all(),
            'userSensor' : userD,
        }
        return render(request, 'secondP.html', context)
    
    else:
        return redirect("/login")
