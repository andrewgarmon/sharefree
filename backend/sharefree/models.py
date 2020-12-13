from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length=5, primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)

class Portfolio(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=15)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

class Share(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
    )
    shares = models.PositiveIntegerField

class User(models.Model):
    user = User.objects.create_user