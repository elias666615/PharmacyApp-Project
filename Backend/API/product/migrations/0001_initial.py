# Generated by Django 3.2.7 on 2021-10-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rating', models.FloatField(default=2.5)),
                ('rating_num', models.PositiveIntegerField(default=0)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='')),
                ('discount', models.FloatField(default=0.0)),
                ('initial_quantity', models.PositiveBigIntegerField()),
                ('sold_quantity', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
