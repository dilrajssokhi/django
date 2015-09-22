# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_director', models.CharField(max_length=200)),
                ('movie_99popularity', models.DecimalField(max_digits=3, decimal_places=1)),
                ('movie_imdbscore', models.DecimalField(max_digits=2, decimal_places=1)),
                ('entry_date', models.DateTimeField(verbose_name=b'date entered')),
            ],
        ),
    ]
