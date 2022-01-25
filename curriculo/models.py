from django.db import models


class Desenvolvedor(models.Model):
    nome_desenvolvedor = models.CharField(max_length=255)
    foto_perfil = models.ImageField(upload_to='fotos_perfil', blank=True)
    titulo_desenvolvedor = models.CharField(max_length=255)
    email_desenvolvedor = models.CharField(max_length=255)
    linkedin_desenvolvedor = models.URLField()
    github_desenvolvedor = models.URLField()
    descricao_desenvolvedor = models.CharField(max_length=255)


class AreaAtuacao(models.Model):
    dev_nome = models.ForeignKey(Desenvolvedor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)


class Habilidades(models.Model):
    desenvolvedor = models.ForeignKey(Desenvolvedor, on_delete=models.CASCADE)
    habilidade = models.CharField(max_length=255)
    is_top_3 = models.BooleanField(default=False)
    is_tec = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)


