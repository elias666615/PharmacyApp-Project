# Generated by Django 3.2.9 on 2021-12-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_rating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]