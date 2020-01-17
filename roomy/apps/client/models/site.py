from django.db import models
from ...commons.common_models           import SingletonModel
class FAQ(models.Model):
    order = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=128)
    message = models.TextField(max_length=256)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label="client"


class ExternalLink(models.Model):
    name = models.CharField(max_length=32)
    icon = models.ImageField(upload_to="files")

    def __str__(self):
        return f'{self.name}'

class Site(SingletonModel):
    title = models.CharField(max_length=32)
    links = models.ManyToManyField(ExternalLink)

    def __str__(self):
        return f'SITE SETTINGS'
