# Generated by Django 5.0.5 on 2024-05-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.IntegerField(choices=[('0', 'Unavailable'), ('1', 'Available')]),
        ),
    ]
