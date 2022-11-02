from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
	path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
	path('update_profile/', views.update_profile, name='update_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
]