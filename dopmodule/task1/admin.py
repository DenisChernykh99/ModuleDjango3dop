from django.contrib import admin
from .models import Buyer, Game

# Register your models here.

# Админка для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',) # Поля для отображения в списке
    search_fields = ('title',) # Поля для поиска
    list_filter = ('size', 'cost',) # Фильтрация по размеру и цене
    list_per_page = 20 # Кол-во записей на странице


# Админка для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('username', 'balance', 'age',)
    search_fields = ('username',)
    list_filter = ('balance', 'age',)
    list_per_page = 30
    readonly_fields = ('balance',)
