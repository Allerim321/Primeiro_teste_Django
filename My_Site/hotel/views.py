from django.shortcuts import render, HttpResponse
from .models import hotel, quarto, usuario
from .forms import FormAgendamento, FormCadastro, FormLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

def agendamento(request):

    if request.method == "POST":
        form = FormAgendamento(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            
            user = usuario(nome=var_nome, email=var_email)
            user.save()
            
            return HttpResponse("<h1>Obrigado</h1>")

    else:
        form = FormAgendamento()

    return render(request, "reservar_quarto.html", {"form": form})

def cadastro(request):

    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']
        
            user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()
            
            return HttpResponse("<h1>Obrigado</h1>")

    else:
        form = FormCadastro()

    return render(request, "cadastro.html", {"form": form})

def login(request):
    form = FormLogin(request.POST)
    if form.is_valid():
        
        var_user = form.cleaned_data['user']
        var_password = form.cleaned_data['password']
        
        user = authenticate(username=var_user, password=var_password)
        print(user)
        if user is not None:
            return HttpResponse("<h1>Bem vindo</h1>")
        else:
            return HttpResponse("<h1>Dados incorretos</h1>")
    else:
        form = FormLogin()
        
    return render(request, "login.html", {"form": form})