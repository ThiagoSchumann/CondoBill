from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.balance}"
