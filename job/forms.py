from django import forms
from .models import applayer , job

class apply(forms.ModelForm):
    class Meta:
        model = applayer
        fields = ( "name" , "email" , "site" , "cv" , "cover_letter")

class add (forms.ModelForm):
    class Meta:
        model = job
        fields = ('__all__')
        exclude = ('slug', 'owner')


