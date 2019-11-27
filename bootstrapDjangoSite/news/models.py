from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    titulo      = models.CharField(max_length=25)
    resumo      = models.CharField(max_length=100)
    conteudo    = models.TextField(verbose_name="Descrição")
    dataPublicacao  = models.DateField(verbose_name="Data de publicação", auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo + " - " + self.resumo + " - " + str(self.dataPublicacao)
