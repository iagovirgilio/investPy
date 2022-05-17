import requests
from django.shortcuts import render
from .models import Cotacao

def cotacao(request):
    if request.method == 'GET':

        url = "https://api.vatcomply.com/rates?base=USD"
        response = requests.get(url)
        response_json = response.json()

        for index in response_json['rates']:
            if index == 'EUR' or index == 'JPY' or index == 'BRL':

                cotacao = Cotacao.objects.filter(moeda=index).first()

                if cotacao:
                    cotacao.valor = response_json['rates'][index]
                    cotacao.save()
                else:
                    cotacao = Cotacao(moeda=index, valor=response_json['rates'][index])
                    cotacao.save()

        cotacao_list = Cotacao.objects.all()
        print('-' * 100)
        print(cotacao_list)
        print('-' * 100)

    return render(request, 'cotacao.html')
