# Generated by Django 3.2.15 on 2022-08-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milli', '0011_auto_20220811_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artsproducts',
            name='artscatagory',
            field=models.CharField(max_length=50),
        ),
    ]
