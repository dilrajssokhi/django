# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlShortner', '0002_urlshortner_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortner',
            name='short_url',
            field=models.URLField(default='myawesome-url-shortener.com'),
            preserve_default=False,
        ),
    ]
