# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='item',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterUniqueTogether(
            name='shoppinglist',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='aisle',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='purchased',
        ),
    ]
