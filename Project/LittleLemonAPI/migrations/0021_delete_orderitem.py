# Generated by Django 5.0.6 on 2024-05-22 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0020_remove_orders_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]