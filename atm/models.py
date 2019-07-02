from django.db import models


class AbstractModel(models.Model):
    """
    Class for adding fields to all created models

    Fields:
    created - marks the date and time the instance was created
    updated - marks the date and time the instance was updated
    """
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
