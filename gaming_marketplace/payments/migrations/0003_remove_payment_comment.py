# Generated by Django 4.2.5 on 2023-10-13 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='comment',
        ),
    ]
