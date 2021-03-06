# Generated by Django 2.2.12 on 2020-05-24 00:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20200522_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=256, verbose_name='Assunto')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
        ),
        migrations.AddField(
            model_name='grupo',
            name='newsletters',
            field=models.ManyToManyField(to='core.Newsletter'),
        ),
    ]
