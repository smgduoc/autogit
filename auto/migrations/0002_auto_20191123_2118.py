# Generated by Django 2.2.7 on 2019-11-24 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehi',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='vehi',
            name='published_date',
        ),
        migrations.AddField(
            model_name='vehi',
            name='annio',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='vehi',
            name='kilom',
            field=models.IntegerField(default=10),
        ),
    ]
