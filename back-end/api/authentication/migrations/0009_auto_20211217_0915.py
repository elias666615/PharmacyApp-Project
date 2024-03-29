# Generated by Django 3.2.9 on 2021-12-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20211112_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='location',
        ),
        migrations.AddField(
            model_name='store',
            name='account_holder_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='account_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='name_of_bank',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='products_sold',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='store',
            name='rating',
            field=models.FloatField(default=2.5),
        ),
        migrations.AddField(
            model_name='store',
            name='total_revenue',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
