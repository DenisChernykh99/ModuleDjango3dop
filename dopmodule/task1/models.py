from django.db import models


# Create your models here.
# Модель покупателя
class Buyer(models.Model):
    username = models.CharField(max_length=30, unique=True)  # Логин
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.CharField(max_length=3)  # Возраст

    def __str__(self):
        return self.username


# Модель Игры
class Game(models.Model):
    title = models.CharField(max_length=20, unique=True)  # Название
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=8, decimal_places=2)  # Размер файлов
    description = models.TextField(blank=True)  # Описание
    age_limited = models.BooleanField(default=False)  # Возрастное ограничение 18+
    buyer = models.ManyToManyField(Buyer, related_name='Games')

    def __str__(self):
        return self.title

# Применены команды QuerySet в shell:
# Buyer.objects.create(username='Nicovega', balance=20000, age=24)
# Buyer.objects.create(username='Filya', balance=2400, age=15)
# Buyer.objects.create(username='Kuplinov', balance=30500, age=41)
# Game.objects.create(title='World of Warcraft', cost=15000, size=17, description='MMORPG')
# Game.objects.create(title='Dota 2', cost=2500, size=1, description='Popa bol', age_limited=True)
# Game.objects.create(title='Sims 3', cost=50000, size=20, description='Simulyator Jizni')
# Game.objects.filter(title='World of Warcraft').update(age_limited=True)
# a = (Buyer.objects.all())
# Game.objects.get(id=3).buyer.set(a)
# adult_buyers = (Buyer.objects.filter(age__gte=18))
# Game.objects.get(id=2).buyer.set(adult_buyers)
# priority_buyer = (Buyer.objects.get(id=3),)
# Game.objects.get(id=1).buyer.set(priority_buyer)
