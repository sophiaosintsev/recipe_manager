# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0026_remove_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 9, 25, 3, 40, 2, 504614, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
