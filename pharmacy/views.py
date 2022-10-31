from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import response
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Pharmacy
from .forms import PharmacyForm

@require_POST
def create_pharmacy(request):
    form = PharmacyForm(request.POST)
    if form.is_valid:
        form.save()
        return HttpResponse(status=200)
    else:
        return JsonResponse({"errors": form.errors.as_text()}, status=400)

def retrieve_pharmacy(request):
    pharmacy = Pharmacy.objects.all()
    return HttpResponse(serializers.serialize("json",pharmacy), content_type="application/json")

def update_pharmacy(request, id):
	pharm = Pharmacy.objects.get(pk = id)
	form = PharmacyForm(request.POST, pharm=pharm)
	form.save()
	return HttpResponse(status=200)

@require_POST
def delete_pharmacy(request, id):
	pharm = Pharmacy.objects.get(pk = id)
	pharm.delete()
	return HttpResponse(status=200)

def view_crud_page (request):
	form = PharmacyForm()
	return render(request, "pharmacy/crud.html", {'form': form})

def get_crud_form_empty(request):
	form = PharmacyForm()
	return JsonResponse({'form': form.as_div()})

def get_crud_form(request, id):
	pharm = Pharmacy.objects.get(pk = id)
	form = PharmacyForm(pharm=pharm)
	return JsonResponse({'form': form.as_div()})