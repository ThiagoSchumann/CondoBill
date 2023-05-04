from datetime import date

from django.db import models
from api.models import Apartment


class Expense(models.Model):
    class Category(models.IntegerChoices):
        ELECTRICITY = 1, 'Energia'
        WATER = 2, 'Água'
        GAS = 3, 'Gás'
        CLEANING = 4, 'Limpeza'
        GARDENING = 5, 'Jardim'
        RESERVE = 6, 'Reserva'
        OTHER = 7, 'Outro'

    class Type(models.IntegerChoices):
        SHARED = 1, 'Compartilhada'
        EXCLUSIVE = 2, 'Exclusiva'

    description = models.CharField(max_length=50)
    value = models.FloatField()
    category = models.IntegerField(choices=Category.choices, default=Category.OTHER)
    due_date = models.DateField(default=date.today().replace(day=10))
    expense_type = models.IntegerField(choices=Type.choices, default=Type.EXCLUSIVE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, blank=True)
    invoiced = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} - {self.apartment}"
