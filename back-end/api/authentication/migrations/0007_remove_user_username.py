# Generated by Django 3.2.9 on 2021-11-11 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_card_information_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
