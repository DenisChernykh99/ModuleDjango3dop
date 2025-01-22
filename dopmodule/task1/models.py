from django.db import models


# Create your models here.
# Модель покупателя
class Buyer(models.Model):
    username = models.CharField(max_length=30, unique=True)  # Логин
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.CharField(max_length=3)  # Возраст


# Модель Игры
class Game(models.Model):
    title = models.CharField(max_length=20, unique=True)  # Название
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=8, decimal_places=2)  # Размер файлов
    description = models.TextField(blank=True)  # Описание
    age_limited = models.BooleanField(default=False)  # Возрастное ограничение 18+
    buyer = models.ManyToManyField(Buyer, related_name='Games')
