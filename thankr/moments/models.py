from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from thankr.models import TimeStampedModel

# Moment defines a moment entry in Thankr.
class Moment(TimeStampedModel):
    class Meta:
        db_table = 'moments'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, db_column="user_id", null=False)
    title = models.CharField(max_length=1024, null=False)
    text = models.TextField(null=False)
    category = models.ForeignKey('Category', max_length=1024, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

class Category(models.Model):
    class Meta:
        db_table = 'categories'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, null=False)
