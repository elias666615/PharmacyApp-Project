# Generated by Django 3.2.9 on 2021-11-22 15:01

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=product.models.upload_to, verbose_name='image'),
        ),
    ]