from warnings import filters
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from apporion.api import serializers
from apporion import models
from django.contrib.auth.models import User
from django_filters import rest_framework as filters


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaSerializer
    queryset = models.empresa.objects.all()

class DetalhesUsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.detalhes_usuariosSerializer
    queryset = models.detalhes_usuarios.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['ID_USUARIO']
    search_fields = ['ID_USUARIO']



class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientesSerializer
    queryset = models.clientes.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['ID_EMPRESA','NOME_FANTASIA','RAZAO_SOCIAL','CNPJ','DATA_ABERTURA','TELEFONE','EMAIL']
    search_fields = ['ID_EMPRESA','NOME_FANTASIA','RAZAO_SOCIAL','CNPJ','DATA_ABERTURA','TELEFONE','EMAIL']

class ItemClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemClientesSerializer
    queryset = models.itemcliente.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID_CLIENTE']

class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutosSerializer
    queryset = models.produtos.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID_PRODUTO','NM_PRODUTO','ATIVO','ID_EMPRESA']

class ServicosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServicosSerializer
    queryset = models.servicos.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID_SERVICO','NM_SERVICO','ATIVO','ID_EMPRESA']

class FormaPgtoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemClientesSerializer
    queryset = models.formas_de_pagamento.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ID_FORMAPGTO','NM_FORMAPGTO','ATIVO','ID_EMPRESA']

# filtros de pesquisa de vendas
class MetricFilter(filters.FilterSet):
    DATA_VENDA = filters.DateFromToRangeFilter()
    search_fields =['ID_EMPRESA','DATA_VENDA','DT_EMBARQUE','ID_CLIENTES','NM_CLIENTE','ID_OPERADORA', 'NM_OPERADORA','REEMBOLSO','REEMBOLSO']

    class Meta:
        model = models.vendas
        fields = ['ID_EMPRESA','DATA_VENDA','DT_EMBARQUE','ID_CLIENTES','NM_CLIENTE','ID_OPERADORA', 'NM_OPERADORA','REEMBOLSO','REEMBOLSO']


class VendasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VendasSerializer
    queryset = models.vendas.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MetricFilter

class OperadoraViewSet(viewsets.ModelViewSet):
    filtros = ['NOME_FANTASIA','RAZAO_SOCIAL','CNPJ','DATA_ABERTURA','TELEFONE','EMAIL','ID_OPERADORA']
    serializer_class = serializers.OperadorasSerializer
    queryset = models.operadoras.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = filtros
    search_fields = filtros


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username','is_staff']


