from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from addresses.models import Address
from django.core.validators import RegexValidator

class Company(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    info = models.CharField(max_length=140)
    name = models.CharField(max_length=100)
    corporate_type = models.CharField(max_length=1)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    website = models.URLField(max_length=30)
    email = models.EmailField(max_length=60)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    emp_count  = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering=["-timestamp"]