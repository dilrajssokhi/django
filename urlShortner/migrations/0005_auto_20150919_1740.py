# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlShortner', '0004_auto_20150919_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlshortner',
            old_name='url',
            new_name='fullurl',
        ),
        migrations.RenameField(
            model_name='urlshortner',
            old_name='url_short',
            new_name='shorturl',
        ),
    ]
