from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paso1', views.paso1, name='paso1'),
]
