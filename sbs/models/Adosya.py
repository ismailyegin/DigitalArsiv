from django.db import models
from sbs.models.Aevrak import Aevrak
from sbs.models.Aklasor import Aklasor
class Adosya(models.Model):
    sirano = models.IntegerField(null=True, blank=True)
    klasor = models.ForeignKey(Aklasor, on_delete=models.DO_NOTHING,null=True, blank=True)
    evrak=models.ManyToManyField(Aevrak)
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)
