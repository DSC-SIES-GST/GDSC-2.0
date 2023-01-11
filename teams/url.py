from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='teams'),
    path('<str:slug>', views.team, name='team'),
]