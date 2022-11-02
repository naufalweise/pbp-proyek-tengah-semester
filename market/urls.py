from django.urls import path
from .views import show_market
from .views import show_json
from .views import add_promo
from .views import delete_promo

app_name = 'market'

urlpatterns = [
    path('', show_market, name='show_market'),
    path('json/', show_json, name='show_json'),
    path('add/', add_promo, name='add_promo'),
    path('delete/<int:id>', delete_promo, name='delete_promo'),
]