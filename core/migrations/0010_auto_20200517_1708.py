# Generated by Django 2.2.12 on 2020-05-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200517_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='link',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Link do Projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Nome'),
        ),
    ]
