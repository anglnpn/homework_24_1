# Generated by Django 5.0.1 on 2024-02-10 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'verbose_name': 'платеж'},
        ),
    ]
