# Generated by Django 3.2.9 on 2021-12-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20211218_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='overall_rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]