from django.db import models
from uuid import uuid4

# Tabela empresa.
class empresa(models.Model):
   ID_EMPRESA = models.UUIDField(primary_key=True, default=uuid4, editable=False)
   NOME_FANTASIA = models.CharField(max_length=255)
   RAZAO_SOCIAL = models.CharField(max_length=255)
   CNPJ = models.CharField(max_length=14)
   STATUS = models.CharField(max_length=10)
   CNAE_PRINCIPAL_DESCRICAO = models.CharField(max_length=255)
   CNAE_PRINCIPAL_CODIGO = models.IntegerField(null=True)
   CEP = models.CharField(max_length=11)
   DATA_ABERTURA = models.DateField(null=True)
   DDD = models.IntegerField(default=0)
   TELEFONE = models.CharField(max_length=14)
   EMAIL = models.EmailField(max_length=254)
   TIPO_LOGRADOURO = models.CharField(max_length=20)
   LOGRADOURO = models.CharField(max_length=255)
   NUMERO = models.CharField(max_length=20)
   COMPLEMENTO = models.CharField(max_length=255)
   BAIRRO = models.CharField(max_length=255)
   MUNICIPIO = models.CharField(max_length=150)
   UF = models.CharField(max_length=2)
   LOGOMARCA = models.TextField(null=True)
   LIBERADO_SISTEMA = models.BooleanField(default=True)
   DADOS_BANCARIOS = models.CharField(max_length=100, default="Não informado")

   # Tabela Usuarios
class detalhes_usuarios(models.Model):
    ID_USUARIO = models.IntegerField(default=0)
    ID_EMPRESA = models.UUIDField()
    NM_USUARIO = models.CharField(max_length=255)
    FOTO = models.TextField(null=True)

   # Tabela Clientes
class clientes(models.Model):
    ID_CLIENTE = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    NOME_FANTASIA = models.CharField(max_length=255)
    RAZAO_SOCIAL = models.CharField(max_length=255)
    CNPJ = models.CharField(max_length=14)
    STATUS = models.CharField(max_length=10)
    CNAE_PRINCIPAL_DESCRICAO = models.CharField(max_length=255)
    CNAE_PRINCIPAL_CODIGO = models.IntegerField(null=True)
    CEP = models.CharField(max_length=11)
    DATA_ABERTURA = models.DateField(null=True)
    DDD = models.IntegerField(default=0)
    TELEFONE = models.CharField(max_length=14)
    EMAIL = models.EmailField(max_length=254)
    TIPO_LOGRADOURO = models.CharField(max_length=20)
    LOGRADOURO = models.CharField(max_length=255)
    NUMERO = models.CharField(max_length=20)
    COMPLEMENTO = models.CharField(max_length=255)
    BAIRRO = models.CharField(max_length=255)
    MUNICIPIO = models.CharField(max_length=150)
    UF = models.CharField(max_length=2)
    FOTO = models.TextField(null=True)
    LIBERADO_SISTEMA = models.BooleanField(default=True)
    ID_EMPRESA = models.UUIDField(default=0)
    DADOS_BANCARIOS = models.CharField(max_length=100, default="Não informado")

   # Tabela para anexar items Base64 no banco de dados
class itemcliente(models.Model):
    ID_ITEM = models.AutoField(primary_key=True, editable=False)
    ID_CLIENTE = models.UUIDField(default=0)
    ARQUIVO_BASE64 = models.TextField()
    DATA_INCLUSAO = models.DateTimeField(auto_now_add=True, null=True)

    # Tabela de produtos
class produtos(models.Model):
    ID_PRODUTO = models.AutoField(primary_key=True, editable=False)
    NM_PRODUTO = models.CharField(max_length=155)
    ATIVO = models.BooleanField(default=True)
    ID_EMPRESA = models.UUIDField(default=0)

    # Tabela Serviços
class servicos(models.Model):
    ID_SERVICO = models.AutoField(primary_key=True, editable=False)
    NM_SERVICO = models.CharField(max_length=155)
    ATIVO = models.BooleanField(default=True)
    ID_EMPRESA = models.UUIDField(default=0)

    # Tabela formas de pagamento
class formas_de_pagamento(models.Model):
    ID_FORMAPGTO = models.AutoField(primary_key=True, editable=False)
    NM_FORMAPGTO = models.CharField(max_length=155)
    ATIVO = models.BooleanField(default=True)
    ID_EMPRESA = models.UUIDField(default=0)

    # Tabela vendas

class vendas(models.Model):
    ID_VENDA = models.AutoField(primary_key=True, editable=False)
    ID_EMPRESA = models.UUIDField(default=0)
    ID_PRODUTO = models.IntegerField(default=0)
    NM_PRODUTO = models.CharField(max_length=155)
    ID_SERVICO = models.IntegerField(default=0)
    NM_SERVICO = models.CharField(max_length=155)
    ID_FORMAPGTO = models.IntegerField(default=0)
    NM_FORMAPGTO = models.CharField(max_length=155)
    ID_CLIENTES = models.UUIDField(default=0)
    NM_CLIENTE = models.CharField(max_length=155)
    ID_OPERADORA = models.IntegerField(default=0)
    NM_OPERADORA = models.CharField(max_length=155)
    VR_TOTAL = models.DecimalField(max_digits = 15, decimal_places = 2, default=0) 
    VR_TAXAS = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    VR_DESCONTO = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    VR_ABATIMENTOS = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    PORCENTAGEM_COMISSAO = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    VR_COMISSAO = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    VR_ENTRADA = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    VR_PARCELADO = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    VR_SALDO = models.DecimalField(max_digits = 15, decimal_places = 2, default=0)
    NR_RESERVA = models.CharField(max_length=30, default="0")
    DT_EMBARQUE = models.DateField(null=True)
    DT_RETORNO = models.DateField(null=True)
    REEMBOLSO = models.BooleanField(default=False)
    COMISSAO_RECEBIDA = models.BooleanField(default=False)
    DT_PGTO_COMISSAO = models.DateField(null=True)
    TIPO_RECEBIMENTO = models.CharField(max_length=30, default="0")
    DATA_VENDA = models.DateField(auto_now_add=True, null=True)
    DATA_CANCELAMENTO = models.DateField(null=True)
    STATUS = models.BooleanField(default=False)
    MOTIVO_CANCELAMENTO = models.CharField(max_length=200,null=True)

class operadoras(models.Model):
    ID_OPERADORA =models.AutoField(primary_key=True, editable=False)
    NOME_FANTASIA = models.CharField(max_length=255)
    RAZAO_SOCIAL = models.CharField(max_length=255)
    CNPJ = models.CharField(max_length=14)
    STATUS = models.CharField(max_length=10)
    CNAE_PRINCIPAL_DESCRICAO = models.CharField(max_length=255)
    CNAE_PRINCIPAL_CODIGO = models.IntegerField(default=0)
    CEP = models.CharField(max_length=11)
    DATA_ABERTURA = models.DateField(null=True)
    DDD = models.IntegerField(default=0)
    TELEFONE = models.CharField(max_length=14)
    EMAIL = models.EmailField(max_length=254)
    TIPO_LOGRADOURO = models.CharField(max_length=20)
    LOGRADOURO = models.CharField(max_length=255)
    NUMERO = models.CharField(max_length=20)
    COMPLEMENTO = models.CharField(max_length=255)
    BAIRRO = models.CharField(max_length=255)
    MUNICIPIO = models.CharField(max_length=150)
    UF = models.CharField(max_length=2)
    LOGOMARCA = models.TextField(null=True)
    LIBERADO_SISTEMA = models.BooleanField(default=True)











    
