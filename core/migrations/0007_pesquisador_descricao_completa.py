# Generated by Django 2.2.12 on 2020-05-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_sobre_mapa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesquisador',
            name='descricao_completa',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
