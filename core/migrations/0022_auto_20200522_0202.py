# Generated by Django 2.2.12 on 2020-05-22 05:02

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20200522_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacao',
            name='imagem_infraestrutura1',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='imagem_infraestrutura2',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='imagem_infraestrutura3',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='instituicoes',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='linhas',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='pesquisadores',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='portifolio',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='premiacoes',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='projetos',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='publicacoes',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='servicos',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='sobre',
        ),
        migrations.RemoveField(
            model_name='informacao',
            name='tema',
        ),
        migrations.RemoveField(
            model_name='linha',
            name='imagem',
        ),
        migrations.AddField(
            model_name='grupo',
            name='descricao',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='email',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='endereco',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='facebook',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='imagem',
            field=models.ImageField(default=1, upload_to=core.models.caminho),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo',
            name='imagem_infraestrutura1',
            field=models.ImageField(default=1, upload_to=core.models.caminho),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo',
            name='imagem_infraestrutura2',
            field=models.ImageField(default=1, upload_to=core.models.caminho),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo',
            name='imagem_infraestrutura3',
            field=models.ImageField(default=1, upload_to=core.models.caminho),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grupo',
            name='instagram',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='instituicoes',
            field=models.ManyToManyField(to='core.Instituicao'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='linhas',
            field=models.ManyToManyField(to='core.Linha'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='mapa',
            field=models.TextField(blank=True, default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3974.278131225411!2d-42.80071524911858!3d-5.058599352781233!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x77c4de0a93d78d1%3A0xfcf5d4a169075b0!2sUniversidade%20Federal%20do%20Piau%C3%AD!5e0!3m2!1spt-BR!2sbr!4v1589396552722!5m2!1spt-BR!2sbr', null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='nome',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='pesquisadores',
            field=models.ManyToManyField(to='core.Pesquisador'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='portifolio',
            field=models.ManyToManyField(to='core.Portifolio'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='premiacoes',
            field=models.ManyToManyField(to='core.Premiacao'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='projetos',
            field=models.ManyToManyField(to='core.Projeto'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='publicacoes',
            field=models.ManyToManyField(to='core.Publicacao'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='servicos',
            field=models.ManyToManyField(to='core.Servico'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='telefone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='twitter',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='idioma',
            name='sigla',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='informacao',
            name='descricao',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='imagem',
            field=models.ImageField(default=1, upload_to=core.models.caminho),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='imagem',
            field=models.ImageField(default=1, upload_to=core.models.caminho),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pesquisador',
            name='imagem',
            field=models.ImageField(default=1, upload_to=core.models.caminho),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Sobre',
        ),
        migrations.DeleteModel(
            name='Tema',
        ),
    ]
