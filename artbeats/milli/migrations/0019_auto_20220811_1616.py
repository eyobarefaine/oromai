# Generated by Django 3.2.15 on 2022-08-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milli', '0018_alter_artsproducts_artsdescr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artsproducts',
            name='artsimage',
        ),
        migrations.AlterField(
            model_name='artsproducts',
            name='artspath',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
