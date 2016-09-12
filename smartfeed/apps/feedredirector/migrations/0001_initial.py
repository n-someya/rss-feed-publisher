# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(verbose_name='link')),
                ('title', models.TextField(verbose_name='タイトル')),
                ('summary', models.TextField(verbose_name='サマリ')),
                ('updated', models.DateTimeField(verbose_name='更新日時')),
            ],
        ),
    ]
