# Generated by Django 5.0.6 on 2024-05-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0014_remove_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=models.CharField(max_length=250),
        ),
    ]
