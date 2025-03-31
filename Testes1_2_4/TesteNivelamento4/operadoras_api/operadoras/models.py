from django.db import models

# Create your models here.

from django.db import models

class Operadora(models.Model):
    registro_ans = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    modalidade = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    ddd = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True, null=True)
    endereco_eletronico = models.CharField(max_length=255, blank=True, null=True)
    representante = models.CharField(max_length=255)
    cargo_representante = models.CharField(max_length=100)
    data_registro_ans = models.DateField()

    def __str__(self):
        return self.nome_fantasia