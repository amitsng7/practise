from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from zipcodes.models import Zipcode

class Address(models.Model):

    street = models.CharField(max_length=140)
    landmark = models.CharField(max_length=140)
    city = models.CharField(max_length=140)
    zipcode = models.ForeignKey(Zipcode)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return (self.street + " " + self.landmark + " " + self.city)

    def __unicode__(self):
        return (self.street + " " + self.landmark + " " + self.city)

    class Meta:
        ordering=["-timestamp"]
        verbose_name_plural = 'Addresses'