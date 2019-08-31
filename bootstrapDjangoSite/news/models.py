from django.db import models

# Create your models here.
class News(models.Model):
    titulo      = models.CharField(max_length=25)
    resumo      = models.CharField(max_length=100)
    conteudo   = models.TextField(verbose_name="Descrição")
    autor       = models.CharField(max_length=20)
    dataPublicacao  = models.DateField(verbose_name="Data de publicação", auto_now=True)

    def __str__(self):
        return self.titulo + " - " + self.resumo + " - " + self.autor + " - " + str(self.dataPublicacao)
