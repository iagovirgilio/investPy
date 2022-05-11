from . import views
from django.urls import path

urlpatterns = [
    path('moedas/', views.moedas, name='moedas'),
]
