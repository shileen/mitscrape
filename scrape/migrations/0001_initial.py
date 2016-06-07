# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('classes', models.CharField(max_length=10)),
                ('attended', models.CharField(max_length=10)),
                ('absent', models.CharField(max_length=10)),
                ('percent', models.CharField(max_length=10)),
                ('updated', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gpalist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sem', models.CharField(max_length=100)),
                ('gpa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('regno', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
