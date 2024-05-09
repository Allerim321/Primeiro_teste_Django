from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("<h1>oi</h1>")
