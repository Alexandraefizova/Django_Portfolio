from django.contrib import admin
from .models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date_arrive', 'weight', 'height', 'special_signs']


admin.site.register(Animal, AnimalAdmin)
