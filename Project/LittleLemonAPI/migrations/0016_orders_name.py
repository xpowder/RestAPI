# Generated by Django 5.0.6 on 2024-05-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0015_alter_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]