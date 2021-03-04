from django.db import models

from sbs.models.AbirimParametre import AbirimParametre
from sbs.models.Adosya import Adosya


class AdosyaParametre(models.Model):

    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)
    value = models.CharField(max_length=120, null=True, blank=True, verbose_name='value')
    dosya = models.ForeignKey(Adosya, on_delete=models.SET_NULL,null=True, blank=True)
    parametre=models.ForeignKey(AbirimParametre,on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return '%s' % (self.value)