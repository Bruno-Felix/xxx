# Generated by Django 3.0.7 on 2020-06-19 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0009_auto_20200611_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='imagem',
        ),
    ]