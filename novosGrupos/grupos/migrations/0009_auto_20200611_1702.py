# Generated by Django 3.0.7 on 2020-06-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0008_auto_20200611_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome do Artista'),
        ),
        migrations.AlterField(
            model_name='comeback',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome da Música'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome do Grupo'),
        ),
    ]
