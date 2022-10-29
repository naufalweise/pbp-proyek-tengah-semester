from django.shortcuts import render

# Create your views here.
import datetime
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

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

def register_customer(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer_group = Group.objects.get(name="customer")
            user.groups.add(customer_group)
            user.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('accounts:login')
    
    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse( "Username atau password salah!", status=401)
            
        if user.groups.filter(name='app_admin'):
            response = redirect('medicine:view_crud')
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        # if user.groups.filter(name='customer'):
        #    return redirect('customer:homepage)

    context = {}
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')