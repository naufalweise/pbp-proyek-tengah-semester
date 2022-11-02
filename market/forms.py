from django import forms

class CreateMarket(forms.Form):
    promo = forms.CharField(max_length=255)