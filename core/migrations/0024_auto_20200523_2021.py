# Generated by Django 2.2.12 on 2020-05-23 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20200523_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacao',
            name='documentos',
            field=models.ManyToManyField(blank=True, null=True, to='core.Documento'),
        ),
    ]