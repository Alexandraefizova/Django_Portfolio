from django.contrib import admin
from .models import Animal, Home


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', )


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_arrive', 'home')


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Home, HomeAdmin)
