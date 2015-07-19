# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=200)),
                ('detail_place', models.CharField(max_length=500)),
                ('word', models.CharField(max_length=500)),
            ],
        ),
    ]
