# Generated by Django 5.0.4 on 2024-04-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_acept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='is_send',
            field=models.BooleanField(default=False),
        ),
    ]
