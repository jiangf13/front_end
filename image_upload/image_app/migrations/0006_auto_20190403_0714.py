# Generated by Django 2.1.1 on 2019-04-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0005_auto_20190403_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='gender',
            field=models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], null=True),
        ),
    ]
