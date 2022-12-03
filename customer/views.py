
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from customer.forms import CustomerForm, RegistrationForm, ProfileForm
from customer.models import Customer

@csrf_exempt
@require_POST
def register_customer(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        if User.objects.filter(username=username).exists():
           return JsonResponse({"status": False, "message": f'Username {username} sudah ada yang memakai.'})
        user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        customer_group = Group.objects.get(name="customer")
        Customer.objects.create(user_id=user.pk, address=form.cleaned_data['address'], phone=form.cleaned_data['phone'])
        user.groups.add(customer_group)
        user.save()
        return JsonResponse({"status": True, "message": "Berhasil membuat akun!"})
    return JsonResponse({"status": False, "errors": form.errors.as_json(), "message": form.errors.items()[0]})
    


@permission_required('customer.view_customer')
def customer_dashboard (request):
    context = {
        'data' : request.user.customer,
        'email': request.user.email,
        'full_name': request.user.get_full_name(),

    }
   
    return render(request, "customer.html", context)

@permission_required('customer.change_customer')
def edit_profile(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("Berhasil mengedit profile")

    return HttpResponse(form.errors.as_text(), status=400)

@permission_required('customer.change_customer')
def edit_profile_json(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        request.user.first_name = form.cleaned_data['first_name']
        request.user.last_name = form.cleaned_data['last_name']
        request.user.save()
        request.user.customer.address = form.cleaned_data['address']
        request.user.customer.phone = form.cleaned_data['phone']
        request.user.customer.save()
        return JsonResponse({'status': True, 'message': 'Berhasil mengedit profil!'})
    return JsonResponse({'status': False, 'errors': form.errors.as_text(), 'message': 'Gagal mengedit profil.'})

@permission_required('customer.view_customer')
def get_profile(request):
    return JsonResponse({
        'first_name': request.user.first_name, 
        'last_name': request.user.last_name,
        'address': request.user.customer.address,
        'phone': request.user.customer.phone
    })

@permission_required('customer.change_customer')
def view_edit_profile(request):
    form = CustomerForm(instance=request.user.customer)
    return render(request, "customer-profile.html", context={'form': form})
