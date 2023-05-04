from django.db import models
from api.models import Invoice


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_date = models.DateField()
    paid_value = models.FloatField()

    def __str__(self):
        return f"{self.invoice} - {self.paid_value}"
