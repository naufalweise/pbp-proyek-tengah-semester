from socket import fromshare
from django import forms
from .models import Pharmacy

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = ['name','address']
