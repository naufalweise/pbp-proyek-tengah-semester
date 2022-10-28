from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'app_admin/register.html', context)

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse( "Username atau password salah!", status=401)
        return redirect('medicine:view_crud')
        

    context = {}
    return render(request, 'app_admin/login.html', context)

@require_POST
def logout(request):
    auth.logout(request)
    return redirect('login')