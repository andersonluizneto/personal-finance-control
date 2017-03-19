from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    """
        Representa a tabela Categoria
    """
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100, verbose_name='descrição')
    fator = models.IntegerField()

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']

class Subcategoria(models.Model):
    """
        Representa a tabela Subcategoria
    """

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100, verbose_name='descrição')
    tipo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['descricao']


class Lancamento(models.Model):
    """
        Representa a tabela Lançamentos
    """
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)    
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)    
    data_lancamento = models.DateTimeField(default=timezone.now, verbose_name='data de lançamento')
    descricao = models.CharField(max_length=200, verbose_name='descrição')
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Lançamento: %s %s' % (self.descricao, self.valor)

    class Meta:
        ordering = ['data_lancamento']