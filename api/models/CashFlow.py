from django.db import models
from api.models import Account


class CashFlow(models.Model):
    class Type(models.IntegerChoices):
        INFLOW = 1, 'Entradas'
        OUTFLOW = 2, 'Saídas'

    description = models.CharField(max_length=100)
    value = models.FloatField()
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.IntegerField(max_length=10, choices=Type.choices)
    balance = models.FloatField()

    def __str__(self):
        return f"{self.type} - {self.description}"
