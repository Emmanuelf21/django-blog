from django.shortcuts import render, get_list_or_404
from .models import Jogo

# Create your views here.
def jogos_list(request):
    jogos = Jogo.objects.all()
    return render (request, 'jogos/jogos_list.html',{'jogos':jogos})