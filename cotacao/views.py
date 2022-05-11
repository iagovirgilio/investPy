from django.shortcuts import render

def cotacao(request):
    return render(request, 'cotacao.html')
