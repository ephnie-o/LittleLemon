# Generated by Django 5.1.3 on 2024-11-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menutable',
            name='inventory',
            field=models.SmallIntegerField(),
        ),
    ]
