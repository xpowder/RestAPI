# Generated by Django 5.0.6 on 2024-05-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0009_rename_customers_orders_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]