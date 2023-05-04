from django.db import models
from api.models import Person


class Apartment(models.Model):
    number = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


    def __str__(self):
        return f"Apartamento {self.number} - {self.person.name}"
