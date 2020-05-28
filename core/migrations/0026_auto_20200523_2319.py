# Generated by Django 2.2.12 on 2020-05-24 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20200523_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='instituicoes',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='linhas',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='pesquisadores',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='portifolio',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='premiacoes',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='projetos',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='publicacoes',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='servicos',
        ),
        migrations.AddField(
            model_name='informacao',
            name='instituicoes',
            field=models.ManyToManyField(to='core.Instituicao'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='linhas',
            field=models.ManyToManyField(to='core.Linha'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='pesquisadores',
            field=models.ManyToManyField(to='core.Pesquisador'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='portifolio',
            field=models.ManyToManyField(to='core.Portifolio'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='premiacoes',
            field=models.ManyToManyField(to='core.Premiacao'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='projetos',
            field=models.ManyToManyField(to='core.Projeto'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='publicacoes',
            field=models.ManyToManyField(to='core.Publicacao'),
        ),
        migrations.AddField(
            model_name='informacao',
            name='servicos',
            field=models.ManyToManyField(to='core.Servico'),
        ),
    ]