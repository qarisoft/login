# Generated by Django 4.2.1 on 2023-05-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.IntegerField(default=0),
        ),
    ]
