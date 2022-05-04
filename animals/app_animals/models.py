from django.db import models
from django.utils.translation import gettext_lazy as _


class Animal(models.Model):
    """Model animal"""
    name = models.CharField(max_length=50, verbose_name=_('name'))
    age = models.IntegerField(verbose_name=_('age'))
    date_arrive = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    weight = models.IntegerField(verbose_name=_('weight'))
    height = models.IntegerField(verbose_name=_('height'))
    special_signs = models.CharField(max_length=200, verbose_name=_('special_signs'))
    owner = models.ForeignKey('auth.User', related_name='animals', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _('animals')
        verbose_name = _('animal')
