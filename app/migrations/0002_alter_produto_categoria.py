# Generated by Django 4.2.5 on 2023-09-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.TextField(blank=True, max_length=62, null=True),
        ),
    ]
