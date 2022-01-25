from django.db import models


class Tecnologia(models.Model):
    nome_tecnologia = models.CharField(max_length=255)


class Projeto(models.Model):
    screenshot = models.ImageField(upload_to='projetos_screenshots', blank=True)
    titulo_do_projeto = models.CharField(max_length=255)
    tecnologias = models.ManyToManyField(Tecnologia)
    descricao = models.TextField()
