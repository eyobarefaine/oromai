# Generated by Django 3.2.15 on 2022-08-10 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('milli', '0004_auto_20220810_0132'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SometableManager',
            new_name='arts',
        ),
        migrations.DeleteModel(
            name='Sometable',
        ),
    ]
