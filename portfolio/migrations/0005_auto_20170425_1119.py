# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20170419_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='image_width',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to='images/portfolio/projects/', width_field='image_width'),
        ),
    ]
