# Generated by Django 2.2.12 on 2020-05-22 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20200522_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='descricao',
        ),
    ]
