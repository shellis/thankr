from django.db import models

class TimeStampedModel(models.Model):
    class Meta:
        abstract = True
    last_modified = models.DateTimeField(null=False, auto_now=True, editable=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True, editable=False)
