from django.db import models
class Aevrak(models.Model):
    file = models.FileField(null=False, blank=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    operationDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s ' % self.file