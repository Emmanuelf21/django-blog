from . import views
from django.urls import path

urlpatterns = [
    path('', views.jogos_list, name='jogos_list'),
    path('<int:pk>/', views.jogo_detail, name='jogo_detail'),
]
