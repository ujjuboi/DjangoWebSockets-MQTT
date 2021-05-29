from django.shortcuts import redirect, render
from .models import SensorData, UserSensor
from .forms import UserMapForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from firstpage.models import UserGroup
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
import threading

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

def sensorData(request, id):
    print("--------------------------------test1-----------")
    if(request.method == 'GET'):
        if(request.user.is_authenticated):
            x = UserGroup.objects.get(user = request.user).group
            s = encryptUser(request.user, x)
            url = "ws://localhost:8000/ws/data/"+x+"/"+s+"/"
            context = {
                'SensorName' : SensorData.objects.get(pk = id).sensorName,
            'url' : url,
            'idd' : int(id)};
            return render(request, 'thirdP.html', context)
        else:
            return redirect("/login")
    
    elif(request.method == 'POST'):
        print("--------------------------------test1-----------")
        if(request.user.is_authenticated):
            print("--------------------------------test2-----------")
            method = request.POST.get("Method")
            user_group = UserGroup.objects.get(user = request.user)
            x = user_group.group
            s = encryptUser(request.user, x)
            url = "ws://localhost:8000/ws/data/"+x+"/"+s+"/"
            context = {
                'SensorName' : SensorData.objects.get(pk = id).sensorName,
            'url' : url,
            'idd' : id,};
            if(method == 'send'):
                user_group.flag = True
                user_group.save()
                print("--------------------------------test-----------")
                t = threading.Thread(target=eventTrigger,args=(x, )).start()
                return render(request, 'thirdP.html', context)
            elif(method == 'stop'):
                 user_group.flag = False
                 user_group.save()
                 return render(request, 'thirdP.html', context)
        else:
            return redirect("/login")


def kill(self):
    self.killed = True

def encryptUser(user, x):
    data = json.dumps({
        'email' : user.email,
        'secret' : x,
    })
    file = open('filekey.key', 'rb')
    key = file.read()
    file.close()
    fernet = Fernet(key)
    encrypt = fernet.encrypt(bytes(data,'utf-8'))
    return encrypt.decode('utf-8')

def eventTrigger(room_name):
    channel_layer = get_channel_layer()
    i = 0
    while i < 10 and UserGroup.objects.get(group = room_name).flag:
        async_to_sync(channel_layer.group_send)(
            'data_%s' % room_name,
            {
                'type': 'chat_message',
                'message': i
            }
        )
        time.sleep(1)
        i+=1

# def closeConnection(room_name):
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_discard)(
#         'data_%s' % room_name,
#         room_name,
#     )
