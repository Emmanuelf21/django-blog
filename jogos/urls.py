from . import views
from django.urls import path

urlpatterns = [
    path('', views.jogos_list, name='jogos_list'),
]
