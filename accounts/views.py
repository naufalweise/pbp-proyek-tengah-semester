from django.shortcuts import render

# Create your views here.
import datetime
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from customer.models import Customer

# Create your views here.
# def register_admin(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             app_admin_group = Group.objects.get(name="app_admin")
#             user.groups.add(app_admin_group)
#             user.save()
#             messages.success(request, 'Akun telah berhasil dibuat!')
#             return redirect('accounts:login')
    
#     context = {'form':form}
#     return render(request, 'accounts/register.html', context)
@csrf_exempt
def register_customer(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer_group = Group.objects.get(name="customer")
            Customer.objects.create(user_id=user.pk, address='-', phone='-')
            user.groups.add(customer_group)
            user.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('accounts:login')
    
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

@csrf_exempt
def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({"errors": "Username atau password salah!"}, status=401)
            
        auth.login(request, user)
        
        if user.groups.filter(name='app_admin'):
            homepage_url = reverse('medicine:view_crud')
            response = JsonResponse({'homepage_url': homepage_url, "user_type": "app_admin"})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        if user.groups.filter(name='customer'):
            homepage_url = reverse('customer:customer_dashboard')
            response = JsonResponse({'homepage_url': homepage_url, "user_type": "customer"})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        else:
            return JsonResponse({"errors": "User tidak punya role!"},status=403)

    context = {}
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

# logout dengan JSON response
@require_POST
def logout_json(request):
    auth.logout(request)
    return JsonResponse({"status": True, "message": "Berhasil logout!"})