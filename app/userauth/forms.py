from django.forms import Form,ModelForm,Widget
from .models import User
from django import forms
from django.core.validators import ValidationError

class loginform(ModelForm):
    class Meta:
        model=User
        fields=['phone','password']
        widgets={
            'phone':forms.TextInput(attrs={'class':'input','placeholder':"账号"}),
            'password':forms.PasswordInput(attrs={'class':'input','placeholder':"密码"}),
        }
    def clean(self):
        clean_data=super().clean()
        phone=clean_data.get('phone',None)
        password=clean_data.get('password',None)
        if password and phone:
            res=User.objects.filter(phone=phone,password=password).first()
            if not res:
                raise ValidationError('用户名或密码错误')
