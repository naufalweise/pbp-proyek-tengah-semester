from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
	path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_edit_profile/', views.view_edit_profile, name='view_edit_profile'),
	
	
]