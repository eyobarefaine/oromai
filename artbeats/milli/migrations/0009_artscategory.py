# Generated by Django 3.2.15 on 2022-08-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milli', '0008_artsproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='artscategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('categorydescr', models.CharField(max_length=50)),
            ],
        ),
    ]