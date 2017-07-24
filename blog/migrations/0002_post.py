# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('content', models.TextField()),
                ('summary', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField()),
                ('last_edited', models.DateTimeField()),
            ],
        ),
    ]