# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('urlShortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 19, 12, 39, 55, 506232, tzinfo=utc), verbose_name=b'date entered'),
            preserve_default=False,
        ),
    ]
