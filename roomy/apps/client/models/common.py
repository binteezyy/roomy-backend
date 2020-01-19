from django.db import models

class City(models.Model):
    name = models.CharField(max_length=56, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label="client"

class Barangay(models.Model):
    name = models.CharField(max_length=56, unique=True)
    city = models.ForeignKey(City,  on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label="client"
