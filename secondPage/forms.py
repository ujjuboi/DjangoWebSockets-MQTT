from django import forms
from .models import UserSensor, SensorData

class UserMapForm(forms.ModelForm):
    
    class Meta:
        model = UserSensor
        fields = ['Uid','Sid']
        labels = {
            'Uid' : 'User Name',
            'Sid' : 'Sensor List'
        }
        
    
    def __init__(self,*args,**kwargs):
        super(UserMapForm,self).__init__(*args,**kwargs)
        self.fields['Uid'].required = False
        self.fields['Uid'].disabled = True
        self.fields['Sid'].required = True
        self.fields['Uid'].widget.attrs.update({
            'class': 'form-control mt-1 ',
        })
        self.fields['Sid'].widget.attrs.update({
            'class': 'form-control mt-1',
            'placeholder' : 'please select'
        })