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
		return JsonResponse({"errors": form.errors.as_text()}, status=400)
	form.save()
	request.session['last_activity'] = "Create Medicine"
	return HttpResponse(status=200)

def retrieve_medicines(request):
	medicines = Medicine.objects.all()
	return HttpResponse(serializers.serialize("json", medicines), content_type="application/json")

@permission_required('medicine.change_medicine')
def update_medicine(request, id):
	instance = Medicine.objects.get(pk = id)
	form = MedicineForm(request.POST, instance=instance)
	form.save()
	request.session['last_activity'] = "Update Medicine"
	return HttpResponse(status=200)

@permission_required('medicine.delete_medicine')
@require_POST
def delete_medicine(request, id):
	instance = Medicine.objects.get(pk = id)
	instance.delete()
	request.session['last_activity'] = "Delete Medicine"
	return HttpResponse(status=200)

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