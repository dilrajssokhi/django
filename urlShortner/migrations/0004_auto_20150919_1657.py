# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlShortner', '0003_urlshortner_short_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshortner',
            name='short_url',
        ),
        migrations.AddField(
            model_name='urlshortner',
            name='url_short',
            field=models.URLField(default=b''),
        ),
    ]
