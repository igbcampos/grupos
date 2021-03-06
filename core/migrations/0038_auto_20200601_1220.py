# Generated by Django 2.2.12 on 2020-06-01 15:20

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20200528_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portifolio',
            name='descricao',
        ),
        migrations.AddField(
            model_name='portifolio',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=core.models.caminho),
        ),
        migrations.AddField(
            model_name='portifolio',
            name='link',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='portifolio',
            name='tipo',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
