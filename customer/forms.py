from django import forms
from .models import Customer
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["id" ,"phone",'address']

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)