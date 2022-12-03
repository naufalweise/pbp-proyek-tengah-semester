from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import response
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Pharmacy
from .forms import PharmacyForm
from django.contrib.auth.decorators import permission_required
from datetime import datetime

@permission_required('pharmacy.add_pharmacy')
@require_POST
def create_pharmacy(request):
    form = PharmacyForm(request.POST)
    if form.is_valid:
        form.save()
        return JsonResponse({"status": 200, "message": "Berhasil menambahkan apotek!"})
    else:
        return JsonResponse({"errors": form.errors.as_text()}, status=400)

def retrieve_pharmacy(request):
    pharmacy = Pharmacy.objects.all()
    return HttpResponse(serializers.serialize("json",pharmacy), content_type="application/json")

@permission_required('pharmacy.change_pharmacy')
def update_pharmacy(request, id):
	pharm = Pharmacy.objects.get(pk = id)
	form = PharmacyForm(request.POST, instance=pharm)
	form.save()
	return JsonResponse({"status": True, "message": "Berhasil mengedit apotek!"})

@permission_required('pharmacy.delete_pharmacy')
@require_POST
def delete_pharmacy(request, id):
	pharm = Pharmacy.objects.get(pk = id)
	pharm.delete()
	return JsonResponse({"status": True, "message": "Berhasil menghapus apotek!"})

@permission_required('pharmacy.change_pharmacy')
def view_crud_page (request):
	form = PharmacyForm()
	return render(request, "pharmacy/crud.html", {'form': form})

@permission_required('pharmacy.add_pharmacy')
def get_crud_form_empty(request):
	form = PharmacyForm()
	return JsonResponse({'form': form.as_div()})

@permission_required('pharmacy.change_pharmacy')
def get_crud_form(request, id):
	pharm = Pharmacy.objects.get(pk = id)
	form = PharmacyForm(instance=pharm)
	return JsonResponse({'form': form.as_div()})