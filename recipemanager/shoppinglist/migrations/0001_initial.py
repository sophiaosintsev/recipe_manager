# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=60)),
                ('aisle', models.CharField(default=b'CAN', max_length=5, choices=[(b'CAN', b'Choose an aisle'), (b'BBC', b'Baby Care'), (b'BKG', b'Baked Goods'), (b'BKS', b'Baking Supplies'), (b'BCI', b'Basic Cooking Ingredients'), (b'BVR', b'Beverages'), (b'CNF', b'Canned Foods'), (b'CRB', b'Cereal/Breakfast'), (b'CND', b'Condiments & Dressings'), (b'DEM', b'Dairy, Eggs & Milk'), (b'DEL', b'Deli'), (b'ETF', b'Ethnic Foods'), (b'FRF', b'Frozen Foods'), (b'HLB', b'Health & Beauty'), (b'HBS', b'Herbs & Spices'), (b'HHP', b'Household Products'), (b'MFS', b'Meat Fish & Seafood'), (b'NOF', b'Natural/Organic Foods'), (b'OTH', b'Other'), (b'PRB', b'Pasta, Rice & Beans'), (b'PTS', b'Pet Supplies'), (b'PRO', b'Produce'), (b'SNS', b'Snacks & Sweets'), (b'SOU', b'Soup')])),
                ('purchased', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='shoppinglist',
            unique_together=set([('user', 'item')]),
        ),
    ]
