from django.db import models

class Noticia(models.Model):

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    titulo = models.CharField('titulo', max_length=128)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField()
    data_publicacao = models.DateTimeField()
    publicado = models.BooleanField()

        
                