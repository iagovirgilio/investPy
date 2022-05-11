from django.shortcuts import render

def moedas(request):
    return render(request, 'moedas.html')
