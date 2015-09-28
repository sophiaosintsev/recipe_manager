# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20150916_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default=b'/static/media/images/default_256.png', null=True, upload_to=b'images', blank=True),
        ),
    ]
