from django.urls import path
from . import views

app_name = "aritimetica"
urlpatterns = [
    path('', views.index),
    path('somar', views.somar, name='somar'),
    path('subtrair', views.subtrair, name='subtrair'),
    path('multiplicar', views.multiplicar, name='multiplicar'),
    path('dividir', views.dividir, name='dividir')
]