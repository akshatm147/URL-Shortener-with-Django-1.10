from django.db import models

# Create your models here.
from shortener.models import MyUrl


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, MyUrl):
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(MyUrl)
    count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
