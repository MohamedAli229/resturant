# Generated by Django 5.0.3 on 2024-04-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturnat', '0002_rename_appointment_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quote', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
