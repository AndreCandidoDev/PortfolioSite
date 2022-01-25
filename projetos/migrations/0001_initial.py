# Generated by Django 3.2.11 on 2022-01-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tecnologia', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(blank=True, upload_to='projetos_screenshots')),
                ('titulo_do_projeto', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('tecnologias', models.ManyToManyField(to='projetos.Tecnologia')),
            ],
        ),
    ]