from django.shortcuts import render
from .models import Estacao
from django.conf import settings

def map_view(request):
    estacoes = Estacao.objects.all()  # ou qualquer outra lógica para pegar as estações
    return render(request, 'mapapp/map.html', {
        'estacoes': estacoes,
        'api_key': settings.GOOGLE_MAPS_API_KEY
    })


