# Generated by Django 4.2.5 on 2023-09-20 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='foto',
            new_name='foto_usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='nome_usuario',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]