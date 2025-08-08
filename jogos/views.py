from django.shortcuts import render, get_object_or_404
from .models import Jogo

# Create your views here.
def jogos_list(request):
    jogos = Jogo.objects.all()
    return render (request, 'jogos/jogos_list.html',{'jogos':jogos})

def jogo_detail(request,pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    return render(request, 'jogos/jogos_detail.html',{'jogo':jogo})