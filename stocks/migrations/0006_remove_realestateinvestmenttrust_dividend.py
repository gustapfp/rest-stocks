# Generated by Django 4.1.7 on 2023-03-02 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_realestateinvestmenttrust_dividend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestateinvestmenttrust',
            name='dividend',
        ),
    ]
