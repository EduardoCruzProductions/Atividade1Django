from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome    = models.CharField(max_length=100)
    cpf     = models.CharField(max_length=14)
    email   = models.EmailField(max_length=200)

    def __str__(self):
        return self.nome + " - " + self.cpf + " - " + self.email

class Produto(models.Model):
    titulo          = models.CharField(max_length=200)
    versao          = models.CharField(max_length=5)
    dataLancamento  = models.DateField(verbose_name="Data de Lançamento")
    descricao       = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.titulo + " - " + self.versao + " - " + str(self.dataLancamento)

class Modulo(models.Model):
    nome            = models.CharField(max_length=100)
    dataLancamento  = models.DateField(verbose_name="Data de Lançamento")
    versao          = models.CharField(max_length=5)
    preco           = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço")
    descricao       = models.TextField(verbose_name="Descrição")
    produto         = models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + " - " + self.versao + " - " + str(self.preco) + " - " + str(self.produto)

class Venda(models.Model):
    dataCompra  = models.DateField(verbose_name="Data de Compra", auto_now=True)
    total       = models.DecimalField(max_digits=6, decimal_places=2)
    desconto    = models.DecimalField(max_digits=6, decimal_places=2)
    cliente     = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.dataCompra) + " - " + str(self.total) + " - " + str(self.desconto) + " - " + str(self.cliente)

class ItensVenda(models.Model):
    total       = models.DecimalField(max_digits=6, decimal_places=2)
    desconto    = models.DecimalField(max_digits=6, decimal_places=2)
    modulo      = models.ForeignKey(Modulo, on_delete=models.PROTECT)
    venda       = models.ForeignKey(Venda, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.total) + " - " + str(self.desconto)
    