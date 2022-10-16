from dataclasses import field, fields
from django.forms import ModelForm
from .models import Medicine
class MedicineForm(ModelForm):
	class Meta:
		model = Medicine
		fields = ['name', 'stock']