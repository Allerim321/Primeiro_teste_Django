from django.shortcuts import render, HttpResponse
from .models import hotel, quarto, usuario
from .forms import FormNome

def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all
    context['dados_hotel'] = dados_hotel
    return render(request, 'homepage.html', context)

def quartos(request):
    context = {}
    dados_quarto = quarto.objects.all
    context['dados_quarto'] = dados_quarto
    return render(request, 'quartos.html', context)

def nome(request):
    
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['senha']
            
            user = usuario(nome=var_nome, email=var_email, senha=var_senha)
            user.save()
            
            return HttpResponse("<h1>Obrigado</h1>")

    else:
        form = FormNome()

    return render(request, "reservar_quarto.html", {"form": form})