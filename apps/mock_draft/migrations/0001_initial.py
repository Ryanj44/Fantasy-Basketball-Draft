# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-27 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('position', models.CharField(max_length=45)),
                ('team', models.CharField(max_length=45)),
                ('points', models.DecimalField(decimal_places=1, max_digits=4)),
                ('rebounds', models.DecimalField(decimal_places=1, max_digits=4)),
                ('assists', models.DecimalField(decimal_places=1, max_digits=4)),
                ('steals', models.DecimalField(decimal_places=1, max_digits=4)),
                ('blocks', models.DecimalField(decimal_places=1, max_digits=4)),
                ('turnovers', models.DecimalField(decimal_places=1, max_digits=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('players', models.ManyToManyField(related_name='teams', to='mock_draft.Player')),
            ],
        ),
    ]
