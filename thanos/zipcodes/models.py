from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Zipcode(models.Model):
    zipcode = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.zipcode)

    def __unicode__(self):
        return str(self.zipcode)

    class Meta:
        ordering=["-timestamp"]