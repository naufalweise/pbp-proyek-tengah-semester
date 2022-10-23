from django.urls import path
from . import views

urlpatterns = [
	path('create', views.create_medicine, name='create_medicine'),
	path('retrieve', views.retrieve_medicines, name='retrieve_medicine'),
	path('update', views.update_medicine, name='update_medicine'),
	path('delete', views.delete_medicine, name='delete_medicine'),
	path('crud', views.view_crud_page, name='view_crud'),
	path('form', views.get_crud_form_empty, name='get_crud_form_empty'),
	path('form/<int:id>', views.get_crud_form, name='get_crud_form'),
]