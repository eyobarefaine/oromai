# Generated by Django 3.2.15 on 2022-08-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milli', '0020_auto_20220811_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artsproducts',
            name='artsname',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
