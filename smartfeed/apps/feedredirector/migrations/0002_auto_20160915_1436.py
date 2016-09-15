# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedredirector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(null=True, verbose_name='link')),
                ('title', models.TextField(null=True, verbose_name='タイトル')),
                ('summary', models.TextField(null=True, verbose_name='サマリ')),
                ('updated', models.DateTimeField(null=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True, verbose_name='name')),
            ],
        ),
        migrations.RemoveField(
            model_name='feed',
            name='link',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='title',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='updated',
        ),
        migrations.AddField(
            model_name='feed',
            name='url',
            field=models.TextField(null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='article',
            name='feed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedredirector.Feed'),
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedredirector.User'),
        ),
    ]
