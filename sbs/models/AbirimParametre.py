from django.db import models

from sbs.models.Abirim import Abirim
from sbs.models.Aevrak import Aevrak
from sbs.services import general_methods


class AbirimParametre(models.Model):
    aDate = 'date'
    aString = 'string'
    aNumber = 'number'
    Type = (
        (aDate, 'Date'),
        (aString, 'String'),
        (aNumber, 'Number'),

    )

    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120,  null=True, blank=True, verbose_name='Başlık')
    type = models.CharField(max_length=128, verbose_name='Türü ', choices=Type,default=aString)
    birim = models.ForeignKey(Abirim, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Birim')

    def __str__(self):
        return '%s' % (self.title)