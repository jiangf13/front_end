# Generated by Django 2.1.1 on 2019-04-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_hotel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='age',
            field=models.IntegerField(default='0'),
        ),
    ]
