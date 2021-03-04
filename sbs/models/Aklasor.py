
from django.db import models

from sbs.models.CategoryItem import CategoryItem
from sbs.models.Abirim import Abirim

class Aklasor(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=120, null=False, blank=False, verbose_name='Tanımı')
    sirano = models.IntegerField(null=False, blank=False,verbose_name='Sıra Numarası')
    location = models.OneToOneField(CategoryItem, on_delete=models.SET_NULL,null=True, blank=True,verbose_name='Konumu')
    birim = models.ForeignKey(Abirim, on_delete=models.SET_NULL,null=True, blank=True,verbose_name='Birim')

    def __str__(self):
        return '%s ' % self.name








