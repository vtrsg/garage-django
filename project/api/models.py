from django.db import models
from django.utils import timezone

class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, blank=True)
    Phone = models.CharField(max_length=50)
    Cpf = models.CharField(max_length=11, unique=True)

class Brand(models.Model):
    Name = models.CharField(max_length=100)

class ModelType(models.Model):
    Name = models.CharField(max_length=100)

class Year(models.Model):
    YearName = models.CharField(max_length=100)

class Car(models.Model):

    STATES = (
        (0, 'Minas Gerais'),
        (1, 'Rio de Janeiro'),
        (2, 'São Paulo'),
    )

    TRANSMISSION = (
        (0, 'Automático'),
        (1, 'Manual'),
    )

    SEATS = (
        (0, '2'),
        (1, '4'),
        (2, '5'),
        (3, '7'),
    )

    FUEL = (
        (0, 'Diesel'),
        (1, 'Flex'),
        (2, 'Gasolina'),
        (3, 'Gasolina Regular'),
        (2, 'Elétrico'),
        (2, 'Híbrido'),
    )

    Name = models.CharField(max_length=100)
    Brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    Model = models.ForeignKey(ModelType, on_delete=models.SET_NULL, blank=True, null=True)
    Year = models.ForeignKey(Year, on_delete=models.SET_NULL, blank=True, null=True)
    Location = models.PositiveSmallIntegerField(choices=STATES)
    Transmission = models.PositiveSmallIntegerField(choices=TRANSMISSION)
    Price = models.FloatField()
    DiscountPrice = models.FloatField(blank=True, null=True)
    Mileage = models.FloatField()
    Color = models.CharField(max_length=100)
    Seat = models.PositiveSmallIntegerField(choices=SEATS)
    Fuel = models.PositiveSmallIntegerField(choices=FUEL)
    CreatedDate = models.DateField(default=timezone.now)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    ImageFile = models.CharField(max_length=100)
