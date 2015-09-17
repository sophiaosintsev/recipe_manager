# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20150910_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='source',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(help_text=b'Number each set of directions'),
        ),
    ]
