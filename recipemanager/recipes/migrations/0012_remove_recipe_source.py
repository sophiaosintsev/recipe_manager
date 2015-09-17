# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20150911_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='source',
        ),
    ]
