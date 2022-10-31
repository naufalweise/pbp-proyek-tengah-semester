from django.urls import path
from pharmacy.views import *
app_name = 'pharmacy'

urlpatterns = [
    path('create', create_pharmacy, name='create_pharmacy'),
    path('retrieve', retrieve_pharmacy, name='retrieve_pharmacy'),
	path('update/<int:id>', update_pharmacy, name='update_pharmacy'),
	path('delete/<int:id>', delete_pharmacy, name='delete_pharmacy'),
	path('crud', view_crud_page, name='view_crud'),
	path('form', get_crud_form_empty, name='get_crud_form_empty'),
	path('form/<int:id>', get_crud_form, name='get_crud_form'),
]