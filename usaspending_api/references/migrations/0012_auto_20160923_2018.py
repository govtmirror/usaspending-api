# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0011_auto_20160922_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtieragency',
            name='agency',
        ),
        migrations.AddField(
            model_name='agency',
            name='aac_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_departments', to='references.Agency'),
        ),
        migrations.AddField(
            model_name='agency',
            name='fourcc_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='agency',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.Location'),
        ),
        migrations.AddField(
            model_name='agency',
            name='parent_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_agencies', to='references.Agency'),
        ),
        migrations.AddField(
            model_name='agency',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='SubtierAgency',
        ),
    ]