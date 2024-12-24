from django.db import models


class Cotacao(models.Model):
    moeda = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.moeda
