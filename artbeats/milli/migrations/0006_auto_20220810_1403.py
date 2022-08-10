# Generated by Django 3.2.15 on 2022-08-10 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('milli', '0005_auto_20220810_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='arts',
            name='descr',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arts',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]