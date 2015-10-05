from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    CATEGORY_CHOICES = (
        ('APP', 'Appetizer'),
        ('BRK', 'Breakfast & Brunch'),
        ('DES', 'Dessert'),
        ('SLD', 'Salad'),
        ('SOP', 'Soup'),
        ('BRD', 'Bread'),
        ('MND', 'Main Dish'),
        ('SDD', 'Side Dish'),
        ('MTP', 'Meat & Poultry'),
        ('SFD', 'Seafood'),
        ('DRK', 'Drink'),
        ('SDW', 'Sandwich')
    )
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default='APP',
    )
    ingredients = models.TextField(
        blank=False,
        help_text='One ingredient per line'
    )
    directions = models.TextField(
        blank=False,
        help_text='Number each set of directions'
    )
    photo = models.ImageField(
        upload_to='images',
        default='images/default_256.png',
        null=False, blank=True,
    )
    # user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return self.title

