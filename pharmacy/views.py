from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from .models import Pharmacy, Medicine
from .forms import MedicineForm
from django.http import HTTPResponse, JsonResponse

# Create your views here.
def get_pharmacy_medicines(request, pharmacy_id):
	medicines = Medicine.objects.filter(pharmacy__pk=pharmacy_id)
	return JsonResponse(medicines)

# TODO: add pharmacy field
def new_medicine(request):
	form = MedicineForm(request.POST)
	if form.is_valid():
		form.save()
		return HTTPResponse("Berhasil menambahkan obat! ")
	return HTTPResponse("Data tidak valid!", status=400)

def edit_medicine(request, medicine_id):
	try:
		medicine = Medicine.objects.get(pk=medicine_id)
		form = MedicineForm(request.POST, instance=medicine)
		if form.is_valid():
			form.save()
			return HTTPResponse("Berhasil mengedit obat!")
		return HTTPResponse("Data tidak valid!", status=400)
	except Medicine.DoesNotExist:
		return HTTPResponse("Id obat tidak ditemukan!", status=400)


def delete_medicine(request, medicine_id):
	try:
		medicine = Medicine.objects.get(pk=medicine_id)
		medicine.delete()
		return HTTPResponse("Berhasil menghapus obat!")
	except Medicine.DoesNotExist:
		return HTTPResponse("Id obat tidak ditemukan!", status=400)

	
