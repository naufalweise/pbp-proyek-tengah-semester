from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import MedicineForm
from .models import Medicine

# Create your views here.
@permission_required('medicine.add_medicine')
@require_POST
def create_medicine(request):
	form = MedicineForm(request.POST)
	if not form.is_valid():
		return JsonResponse({"status": False, "errors": form.errors.as_text(), "message": "Gagal menambahkan obat."}, status=400)
	form.save()
	request.session['last_activity'] = "Create Medicine"
	return JsonResponse({"status":True, "message": "Berhasil menambahkan obat!"});

def retrieve_medicines(request):
	medicines = Medicine.objects.all()
	medicines_data = list(map(serialize_medicine, medicines))
	return JsonResponse(medicines_data, safe=False)
	
def serialize_medicine(medicine):
	obj = {}
	obj['pk'] = medicine.pk
	obj['fields'] = {}
	obj['fields']['name'] = medicine.name
	obj['fields']['stock'] = medicine.stock
	obj['fields']['pharmacy'] = medicine.pharmacy.name
	obj['fields']['pharmacy_id'] = medicine.pharmacy.id
	return obj

def retrieve_medicines_detailed(request):
	medicines = Medicine.objects.all()
	medicines_data = map(serialize_medicine, medicines)
	return JsonResponse(list(medicines_data), safe=False)


	
def add_pharmacy_name(medicine):
	medicine['pharmacy_name'] = medicine

@permission_required('medicine.change_medicine')
def update_medicine(request, id):
	instance = Medicine.objects.get(pk = id)
	form = MedicineForm(request.POST, instance=instance)
	form.save()
	request.session['last_activity'] = "Update Medicine"
	return JsonResponse({"status": True, "message": "Berhasil mengedit obat!"})

@permission_required('medicine.delete_medicine')
@require_POST
def delete_medicine(request, id):
	instance = Medicine.objects.get(pk = id)
	instance.delete()
	request.session['last_activity'] = "Delete Medicine"
	return JsonResponse({"status": True, "message": "Berhasil menghapus obat!"})

@permission_required('medicine.change_medicine')
def view_crud_page (request):
	form = MedicineForm()
	return render(request, "medicine/crud.html", {'form': form})

@permission_required('medicine.add_medicine')
def get_crud_form_empty(request):
	form = MedicineForm()
	return JsonResponse({'form': form.as_div()})

@permission_required('medicine.change_medicine')
def get_crud_form(request, id):
	instance = Medicine.objects.get(pk = id)
	form = MedicineForm(instance=instance)
	request.session['last_activity_date'] = str(datetime.now())
	return JsonResponse({'form': form.as_div()})