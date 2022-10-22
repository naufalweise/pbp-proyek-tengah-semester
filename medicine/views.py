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
		return HttpResponse(status_code=400)
	form.save()
	return HttpResponse(status_code=200)
	pass

def retrieve_medicines():
	pass

def update_medicine():
	pass

def delete_medicine():
	pass


def view_crud_page (request):
	form = MedicineForm()
	return render(request, "medicine/crud.html", {'form': form})

def get_crud_form(request, id):
	form
	if id is None:
		form = MedicineForm()
	else:
		instance = Medicine.objects.get(pk = id)
		form = MedicineForm(instance=instance)
	return JsonResponse({'form': form})