from datetime import timezone

from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from django.urls import reverse


class Animal(SafeDeleteModel):
    """Параметры животного"""
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField('Кличка', max_length=50)
    age = models.IntegerField('Возраст', default=0)
    date_arrive = models.DateTimeField('Дата прибытия', auto_now_add=True)
    weight = models.IntegerField('Вес', default=0)
    growth = models.IntegerField('Рост', default=0)
    special_signs = models.TextField('Особые приметы')
    home = models.ForeignKey('Home', on_delete=models.PROTECT, verbose_name="Приют", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
        ordering = ['-date_arrive', ]


class Home(SafeDeleteModel):
    """Модель приюта"""
    _safedelete_policy = SOFT_DELETE_CASCADE
    title = models.CharField(max_length=200, db_index=True, verbose_name="Наименование приюта")

    class Meta:
        verbose_name = 'Приют'
        verbose_name_plural = 'Приюты'
