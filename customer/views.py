
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from customer.models import Customer


@login_required(login_url='/accounts/login/')
# Create your views here.
def update_profile (request, pk):
    current_user = request.user
    if request.method == 'POST':
        get_email = request.POST.get('email', '').strip()
        get_first = request.POST.get('first_name', '').strip()
        get_last = request.POST.get('last_name', '').strip()
        get_phone = request.POST.get('phone', '').strip()
        get_address = request.POST.get('address', '').strip()
        suspect.objects.filter(pk=current_user.pk).update(username=get_email)

        return HttpResponse('Profile Updated')
    else:
        return render(request, 'prorile_update_form.html', {'current_user': current_user})

@login_required(login_url='/accounts/login/')
def customer_dashboard (request):
    data_cust = Customer.objects.filter(user=request.user)
    context = {
        'data' : data_cust,
        'email': request.user.email,
        'full_name': request.user.get_full_name(),

    }
   
    return render(request, "customer.html", context)


def create_profile(request):
    pass