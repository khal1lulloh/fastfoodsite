# Generated by Django 4.0.6 on 2022-08-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=9),
        ),
    ]
