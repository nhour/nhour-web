# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 12:41
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(validators=[django.core.validators.MaxValueValidator(52), django.core.validators.MinValueValidator(1)])),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)])),
                ('hours', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('comment', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='RegularEntry',
            fields=[
                ('entry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nhour.Entry')),
            ],
            options={
                'verbose_name_plural': 'Regular Entries',
            },
            bases=('nhour.entry',),
        ),
        migrations.CreateModel(
            name='SpecialEntry',
            fields=[
                ('entry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nhour.Entry')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nhour.Activity')),
            ],
            options={
                'verbose_name_plural': 'Special Entries',
            },
            bases=('nhour.entry',),
        ),
        migrations.AddField(
            model_name='project',
            name='related_systems',
            field=models.ManyToManyField(to='nhour.System'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='regularentry',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nhour.Project'),
        ),
        migrations.AddField(
            model_name='regularentry',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nhour.System'),
        ),
        migrations.AddField(
            model_name='regularentry',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nhour.Task'),
        ),
    ]
