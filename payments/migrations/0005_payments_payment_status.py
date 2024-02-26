# Generated by Django 5.0.2 on 2024-02-25 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_alter_payments_payment_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('successes', 'Успешно'), ('failed', 'Неуспешно')], max_length=50, null=True),
        ),
    ]