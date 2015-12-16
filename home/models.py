from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    phone = models.IntegerField()
    good_team = models.BooleanField(default=False)
    good_code = models.BooleanField(default=False)
    other_goods = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
