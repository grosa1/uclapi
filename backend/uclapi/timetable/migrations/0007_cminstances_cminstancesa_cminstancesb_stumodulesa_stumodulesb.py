# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_deptsa_deptsb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cminstances',
            fields=[
                ('setid', models.TextField(max_length=10)),
                ('instid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('instcode', models.TextField(blank=True, max_length=10, null=True)),
                ('instname', models.TextField(blank=True, max_length=40, null=True)),
                ('linkcode', models.TextField(blank=True, max_length=20, null=True)),
                ('instrank', models.BigIntegerField(blank=True, null=True)),
                ('inststart', models.DateField(blank=True, null=True)),
                ('instfinish', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': '"CMIS_OWNER"."CMINSTANCES"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CminstancesA',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('setid', models.TextField(max_length=10)),
                ('instid', models.BigIntegerField(blank=True, null=True)),
                ('instcode', models.TextField(blank=True, max_length=10, null=True)),
                ('instname', models.TextField(blank=True, max_length=40, null=True)),
                ('linkcode', models.TextField(blank=True, max_length=20, null=True)),
                ('instrank', models.BigIntegerField(blank=True, null=True)),
                ('inststart', models.DateField(blank=True, null=True)),
                ('instfinish', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CminstancesB',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('setid', models.TextField(max_length=10)),
                ('instid', models.BigIntegerField(blank=True, null=True)),
                ('instcode', models.TextField(blank=True, max_length=10, null=True)),
                ('instname', models.TextField(blank=True, max_length=40, null=True)),
                ('linkcode', models.TextField(blank=True, max_length=20, null=True)),
                ('instrank', models.BigIntegerField(blank=True, null=True)),
                ('inststart', models.DateField(blank=True, null=True)),
                ('instfinish', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StumodulesA',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('setid', models.TextField(max_length=10)),
                ('studentid', models.TextField(max_length=12)),
                ('deptid', models.TextField(max_length=10)),
                ('moduleid', models.TextField(max_length=12)),
                ('modgrpcode', models.TextField(max_length=10)),
                ('slotid', models.BigIntegerField(blank=True, null=True)),
                ('fixingrp', models.CharField(max_length=1)),
                ('modpart', models.TextField(max_length=10)),
                ('restype', models.TextField(max_length=10)),
                ('unitvalue', models.TextField(max_length=10)),
                ('classif', models.TextField(max_length=10)),
                ('papernum', models.BigIntegerField(blank=True, null=True)),
                ('modlevel', models.TextField(max_length=10)),
                ('inactive', models.CharField(max_length=1)),
                ('instid', models.BigIntegerField(blank=True, null=True)),
                ('courseid', models.TextField(max_length=12)),
                ('crsyear', models.BigIntegerField(blank=True, null=True)),
                ('semid', models.BigIntegerField(blank=True, null=True)),
                ('moddropped', models.CharField(max_length=1)),
                ('donotcount', models.CharField(max_length=1)),
                ('semrank', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StumodulesB',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('setid', models.TextField(max_length=10)),
                ('studentid', models.TextField(max_length=12)),
                ('deptid', models.TextField(max_length=10)),
                ('moduleid', models.TextField(max_length=12)),
                ('modgrpcode', models.TextField(max_length=10)),
                ('slotid', models.BigIntegerField(blank=True, null=True)),
                ('fixingrp', models.CharField(max_length=1)),
                ('modpart', models.TextField(max_length=10)),
                ('restype', models.TextField(max_length=10)),
                ('unitvalue', models.TextField(max_length=10)),
                ('classif', models.TextField(max_length=10)),
                ('papernum', models.BigIntegerField(blank=True, null=True)),
                ('modlevel', models.TextField(max_length=10)),
                ('inactive', models.CharField(max_length=1)),
                ('instid', models.BigIntegerField(blank=True, null=True)),
                ('courseid', models.TextField(max_length=12)),
                ('crsyear', models.BigIntegerField(blank=True, null=True)),
                ('semid', models.BigIntegerField(blank=True, null=True)),
                ('moddropped', models.CharField(max_length=1)),
                ('donotcount', models.CharField(max_length=1)),
                ('semrank', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
