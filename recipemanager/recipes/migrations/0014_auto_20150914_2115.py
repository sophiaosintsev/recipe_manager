# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20150914_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default=b'/recipemanager/static/default_256.png', null=True, upload_to=b'/media/images/', blank=True),
        ),
    ]
