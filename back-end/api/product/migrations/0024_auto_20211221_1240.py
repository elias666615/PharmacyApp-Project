# Generated by Django 3.2.9 on 2021-12-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20211220_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rating_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]