# Generated by Django 5.0.6 on 2024-05-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0018_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
