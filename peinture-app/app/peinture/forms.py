from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import  AuthenticationForm
class CouleurForm(forms.Form):
    marque = forms.ModelChoiceField(queryset=marque.objects.all())
    voiture = forms.ModelChoiceField(queryset=voiture.objects.all())
    color_code = forms.CharField(max_length=30,required=0)
    hex_code = forms.CharField(max_length=6 , required=0)
    name = forms.CharField(max_length=50 , required= 0)


class LoginForm(AuthenticationForm):
    # Add additional fields for login form
    class Meta:
        model = User
        fields = ('username', 'password')



class AjoutcouleurForm(forms.ModelForm):
    model = forms.ModelChoiceField(queryset=voiture.objects.all())
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7,default='') # 6 chiffres hexadécimaux + le symbole #
    color_code = models.CharField(max_length=6,default='')
    class Meta:
        model = couleur
        fields = ['name', 'model', 'hex_code','color_code']