from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('register', views.register_customer, name='register_customer'),
	path('login/', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('logout/json', views.logout_json, name='logout_json'),
]