from django.db import models

class Abirim(models.Model):

    name = models.CharField(max_length=120, null=True, blank=True, verbose_name='name')
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)
