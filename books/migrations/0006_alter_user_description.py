# Generated by Django 4.1.2 on 2023-12-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_user_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]