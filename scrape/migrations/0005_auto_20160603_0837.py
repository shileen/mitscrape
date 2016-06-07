# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_auto_20160603_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='absent',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='classes',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='course_code',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='percent',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='updated',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
