from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paso3', views.paso3, name='paso3'),
]

