# Generated by Django 2.2.5 on 2020-03-05 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0004_remove_destination_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]