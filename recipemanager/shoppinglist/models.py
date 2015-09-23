from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    item = models.CharField(max_length=1000)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user

