import requests
from django.shortcuts import render
from .models import Cotacao
from datetime import datetime, timedelta

def cotacao(request):
    if request.method == 'GET':
        dias = 1
        Cotacao.objects.all().delete()
        while dias < 6:
            data_parametro = (datetime.now() - timedelta(days=dias)).strftime('%Y-%m-%d')
            url = "https://api.vatcomply.com/rates?base=USD&date=" + data_parametro
            response = requests.get(url)
            response_json = response.json()

            for index in response_json['rates']:
                if index == 'EUR' or index == 'JPY' or index == 'BRL':
                    cotacao = Cotacao(moeda=index, valor=response_json['rates'][index], data=data_parametro)
                    cotacao.save()
            dias += 1
            cotacao_list = Cotacao.objects.all()
            print('-' * 100)
            print(cotacao_list)
            print('-' * 100)

    return render(request, 'cotacao.html')
