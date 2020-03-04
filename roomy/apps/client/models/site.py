from django.db import models
from ...commons.common_models           import SingletonModel
from django.db.models.signals import pre_save
from django.dispatch import receiver


class FAQ(models.Model):
    question = models.CharField(max_length=128)
    order = models.PositiveIntegerField(default=0)
    answer = models.TextField(max_length=256)

    def __str__(self):
        return f'({self.pk}){self.question}'

    class Meta:
        app_label="client"


@receiver(pre_save, sender=FAQ)
def faq_order_swap(sender,instance, **kwargs):
    print("ORIGINAL:",instance.order)
    try:
        faq = FAQ.objects.get(order=instance.order)
        if instance.pk != faq.pk:
            temp = instance.order
            instance.order = faq.order
            faq.order = temp

            faq.save()
        elif faq and instance.pk == faq.pk:
            print("SELF")
        else:
            print("GOOD")
    except Exception as e:
        pass
    # instance.save()
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
