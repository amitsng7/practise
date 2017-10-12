from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Company(models.Model):
	# CORPORATE_TYPE = (
	# 	('')
	# 	)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    info = models.CharField(max_length=140)
    name = models.CharField(max_length=100)
    # corporate_type = models.CharField(max_length=1, choices=CORPORATE_TYPE)
    contact = models.IntegerField(max_length=10)
    website = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    emp_count  = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=["-timestamp"]

    # @property
    # def comments(self):
    #     instance = self
    #     qs = Comment.objects.filter_by_instance(instance)
    #     return qs

    # @property
    # def get_content_type(self):
    #     instance = self
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     return content_type