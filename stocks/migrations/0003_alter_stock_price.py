# Generated by Django 4.1.7 on 2023-03-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_rename_stocks_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.FloatField(),
        ),
    ]
