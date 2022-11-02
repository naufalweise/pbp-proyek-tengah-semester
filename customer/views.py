
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse
from customer.forms import CustomerForm
from customer.models import Customer


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
def view_edit_profile(request):
    form = CustomerForm(instance=request.user.customer)
    return render(request, "customer-profile.html", context={'form': form})
