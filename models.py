from django.db import models

class Titulo(models.Model):
    text = models.CharField(max_length = 50)
    def __str__(self):
        return self.text

class Receita(models.Model):
    text = models.CharField(max_length = 200)
    valor = models.IntegerField('Receita mensal', null=True)
    titulo = models.ForeignKey(Titulo, on_delete = models.CASCADE)
    def __str__(self):
        return self.text


class Despesa(models.Model):
    text = models.CharField(max_length = 50)
    valor = models.IntegerField('Despesa mensal', null=True)
    titulo = models.ForeignKey(Titulo, on_delete = models.CASCADE)
    def __str__(self):
        return self.text

class Balanco(models.Model):
    text = models.CharField(max_length = 50)
    receitas = models.ManyToManyField(Receita)
    despesas = models.ManyToManyField(Despesa)
    valor_receita = property(lambda self: sum( rct.valor for rct in self.receitas.all() ))
    valor_despesa = property(lambda self: sum( dps.valor for dps in self.despesas.all() ))
    titulo = models.ForeignKey(Titulo, on_delete = models.CASCADE)
    def __str__(self):
        return self.text
    @property
    def valor_total(self):
        total = self.valor_receita - self.valor_despesa
        return total

class Usuario(models.Model):
    nomeuser = models.CharField(max_length=25)
    senha = models.CharField(max_length=25)
    class Meta:
        verbose_name = 'usuário'
    def __str__(self):
        return self.nomeuser
