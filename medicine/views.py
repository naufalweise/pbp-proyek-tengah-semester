from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import MedicineForm
from .models import Medicine

# Create your views here.
@require_POST
def create_medicine(request):
	form = MedicineForm(request.POST)
	if not form.is_valid():
		return JsonResponse({"errors": form.errors.as_text()}, status=400)
	form.save()
	return HttpResponse(status=200)

def retrieve_medicines(request):
	medicines = Medicine.objects.all()
	return HttpResponse(serializers.serialize("json", medicines), content_type="application/json")

def update_medicine():
	pass

@require_POST
def delete_medicine(request, id):
	instance = Medicine.objects.get(pk = id)
	instance.delete()
	return HttpResponse(status=200)


def view_crud_page (request):
	form = MedicineForm()
	return render(request, "medicine/crud.html", {'form': form})

def get_crud_form_empty(request):
	form = MedicineForm()
	return JsonResponse({'form': form.as_div()})

def get_crud_form(request, id):
	instance = Medicine.objects.get(pk = id)
	form = MedicineForm(instance=instance)
	return JsonResponse({'form': form})