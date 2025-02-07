# Generated by Django 5.0.3 on 2024-09-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=500)),
                ('short_url', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
