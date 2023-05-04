from django.db import models
from api.models import Invoice


class CashFlow(models.Model):
    TYPE_CHOICES = (
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    )

    description = models.CharField(max_length=100)
    value = models.FloatField()
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.description}"
