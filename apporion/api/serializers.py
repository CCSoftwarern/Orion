from rest_framework import serializers
from apporion import models
from django.contrib.auth.models import User

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.empresa
        fields = '__all__'

class detalhes_usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.detalhes_usuarios
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.clientes
        fields = '__all__'
        
class ItemClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.itemcliente
        fields = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.produtos
        fields = '__all__'

class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.servicos
        fields = '__all__'

class FormaPgtosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.formas_de_pagamento
        fields = '__all__'

class VendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.vendas
        fields = '__all__'

class OperadorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.operadoras
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'