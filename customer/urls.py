from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
	path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
	path('profile', views.get_profile, name = 'get_profile'),
	path('profile/edit', views.edit_profile_json, name='edit_profile_json'),
    path('view_edit_profile/', views.view_edit_profile, name='view_edit_profile'),
	path('register', views.register_customer, name='register_customer'),
]