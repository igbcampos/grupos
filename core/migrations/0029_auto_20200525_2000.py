# Generated by Django 2.2.12 on 2020-05-25 23:00

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20200524_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=core.models.caminho),
        ),
        migrations.AlterField(
            model_name='pesquisador',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=core.models.caminho),
        ),
    ]
