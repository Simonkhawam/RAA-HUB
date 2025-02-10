from django.contrib.auth.models import AbstractUser
from django.db import models

class TipStatie(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TipComanda(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StadiulComenzii(models.Model):
    name = models.CharField(max_length=255)
    end_date = models.DateField(null=True, blank=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name

class Utilizator(models.Model):
    prenume = models.CharField(max_length=255, null=False)
    nume = models.CharField(max_length=25, null=False)
    username = models.CharField(max_length=255, unique=True, null=False)
    parola = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    telefon = models.CharField(max_length=255, null=False)
    tip_statie = models.ForeignKey(TipStatie, on_delete=models.CASCADE)

    DEPARTMENT_CHOICES = [
        ('production', 'Production'),
        ('sales', 'Sales'),
    ]
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='production')
    def __str__(self):
        return self.username

class Comanda(models.Model):
    utilizator = models.ForeignKey(Utilizator, on_delete=models.CASCADE)
    status = models.ForeignKey(StadiulComenzii, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    agent_name = models.CharField(max_length=255)
    code_art = models.CharField(max_length=255)
    order_number = models.CharField(max_length=255, unique=True)
    client_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    final_quantity = models.PositiveIntegerField(null=True, blank=True)
    order_type = models.ForeignKey(TipComanda, on_delete=models.SET_NULL, null=True)
    dimension = models.CharField(max_length=255 ,null=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.client_name

