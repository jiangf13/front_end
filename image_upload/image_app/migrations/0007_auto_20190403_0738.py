# Generated by Django 2.1.1 on 2019-04-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0006_auto_20190403_0714'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default='0')),
                ('gender', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], null=True)),
                ('people_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]