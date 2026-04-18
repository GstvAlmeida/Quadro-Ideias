from django.shortcuts import render, redirect
from .models import Conteudo

def home(request):
    if request.method == 'POST':
        titulo_ideia = request.POST.get('titulo')
        categoria = request.POST.get('categoria', 'sugestoes')
        imagem_ideia = request.FILES.get('imagem')

        if titulo_ideia:
            Conteudo.objects.create(
                titulo=titulo_ideia,
                texto="",
                imagem=imagem_ideia if imagem_ideia else None,
                categoria=categoria,
            )
        return redirect('home')

    sugestoes = Conteudo.objects.filter(categoria='sugestoes').order_by('-data_criacao')
    formas = Conteudo.objects.filter(categoria='formas').order_by('-data_criacao')
    elementos = Conteudo.objects.filter(categoria='elementos').order_by('-data_criacao')

    return render(request, 'index.html', {
        'sugestoes': sugestoes,
        'formas': formas,
        'elementos': elementos,
    })