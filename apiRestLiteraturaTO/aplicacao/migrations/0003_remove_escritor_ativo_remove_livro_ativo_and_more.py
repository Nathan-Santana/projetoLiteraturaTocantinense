# Generated by Django 5.0.6 on 2024-05-23 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0002_remove_escritor_atualizacao_remove_escritor_criacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='escritor',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='membro',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='ativo',
        ),
    ]