# Generated by Django 3.2.15 on 2022-08-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milli', '0027_alter_artbeatsproducts_artsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='artsproducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.CharField(max_length=255)),
            ],
        ),
    ]
