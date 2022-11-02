from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Market
from .forms import CreateMarket
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def show_market(request):
    context = {
        'login': 'Login to get Promo Infos!',
        'welcome': 'Welcome to Market',
    }
    return render(request, "market.html", context)

def show_json(request):
    data_market = Market.objects.all()
    return HttpResponse(serializers.serialize('json', data_market), content_type='application/json')

def add_promo(request):
    if request.method == 'POST':
        deal = request.POST.get('deal')
        print(deal)
        new_obj = Market(promo=deal)
        new_obj.save()
        print(deal)
    return JsonResponse({}, status=200)

def delete_promo(request, id):
    if request.method == 'POST':
        Market.objects.filter(id=id).delete()
    return JsonResponse({}, status=200)