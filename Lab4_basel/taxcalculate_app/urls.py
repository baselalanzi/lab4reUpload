
from django.urls import path

from .views import home, calculate_total, tax_rate_view


urlpatterns = [
   
    path('', home, name='home'),
   
    path('taxrate/', tax_rate_view, name='tax_rate'),

     path('<str:number>/', calculate_total, name='calculate_total'),
    
]
