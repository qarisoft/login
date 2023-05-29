# Generated by Django 4.2.1 on 2023-05-29 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Membershib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membershib', to=settings.AUTH_USER_MODEL)),
                ('m_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='membershib', to='users.category')),
            ],
        ),
    ]
