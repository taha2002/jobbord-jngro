from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class Singup_form (UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class pro_edit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        
class us_edit(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name","last_name")

