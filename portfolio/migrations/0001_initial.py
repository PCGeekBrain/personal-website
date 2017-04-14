# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of client to display', max_length=100)),
                ('url', models.URLField(blank=True, help_text='URL to send client to')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title for the project', max_length=35)),
                ('path_name', models.CharField(db_index=True, help_text='/projects/<path_name>', max_length=30)),
                ('short_description', models.TextField(help_text='250 character description of the project for the front page', max_length=250)),
                ('description', models.TextField(help_text='Description displayed detail page')),
                ('starting_date', models.DateField(blank=True, help_text='Optional date range', null=True)),
                ('completion_date', models.DateField()),
                ('url', models.URLField(blank=True, null=True)),
                ('public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modifed', models.DateTimeField(auto_now=True)),
                ('client', models.ManyToManyField(blank=True, to='portfolio.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of position/role', max_length=30)),
                ('slug', models.CharField(help_text='Shorted Version for site navigation', max_length=30)),
                ('description', models.CharField(help_text='For listing', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of skill', max_length=30)),
                ('slug', models.CharField(help_text='Shorted Version for site navigation', max_length=30)),
                ('description', models.CharField(help_text='For listing', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the type of project', max_length=30)),
                ('slug', models.CharField(help_text='Shorted Version for site navigation', max_length=30)),
                ('description', models.CharField(help_text='For listing', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.Type'),
        ),
        migrations.AddField(
            model_name='project',
            name='roles',
            field=models.ManyToManyField(blank=True, to='portfolio.Role'),
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(blank=True, to='portfolio.Skill'),
        ),
    ]
