# Generated by Django 3.1.5 on 2021-01-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210128_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
