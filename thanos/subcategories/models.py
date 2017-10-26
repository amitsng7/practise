from django.conf import settings
from django.db import models
from companies.models import Company
from categories.models import Category
from django.core.validators import RegexValidator

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    category_id = models.ForeignKey(Category)
    company_id = models.ForeignKey(Company)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering=["-timestamp"]
        verbose_name_plural = 'SubCategories'