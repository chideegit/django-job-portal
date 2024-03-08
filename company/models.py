from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=100)
    physical_address = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=(('Lagos', 'Lagos'), ('Abuja', 'Abuja'), ('Kogi', 'Kogi')))
    country = models.CharField(max_length=20, choices=(('Nigeria', 'Nigeria'), ))
    established_on = models.PositiveIntegerField() # year company was established
    employees_total = models.PositiveIntegerField()
    industry = models.CharField(max_length=20, choices=(('Tech', 'Tech'), ('Mining', 'Mining'), ('Health', 'Health')), null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 
    

