from django.db import models

class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created'
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified'
    )
    active = models.BooleanField(
        db_column='cs_active',
        default=True
    )

    class Meta:
        abstract = True
        managed = True


class CategoriaTipo(models.TextChoices):
    RECEITA = '0'
    DESPESA = '1'


class Empresa(ModelBase):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha_hash = models.CharField(max_length=255)


class Usuario(ModelBase):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    empresa_hash = models.CharField(max_length=255)


class Categoria(ModelBase):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(
        max_length=10,
        choices=CategoriaTipo.choices,
        default=CategoriaTipo.RECEITA
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Receita(ModelBase):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Despesa(ModelBase):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Fornecedor(ModelBase):
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Funcionario(ModelBase):
    nome = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class PagamentoFuncionario(ModelBase):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)


class Produto(ModelBase):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)


class Venda(ModelBase):
    data = models.DateField()
    produtos = models.ManyToManyField(Produto)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

