"""
URL configuration for orion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from apporion import views

from rest_framework import routers
from apporion.api import viewsets as apporionsviewsets
from rest_framework.authtoken.views import obtain_auth_token
from apporion.views import CustomAuthToken, AutoCriarEmpresa



route = routers.DefaultRouter(trailing_slash=False)
route.register(r'empresa', apporionsviewsets.EmpresaViewSet, basename="empresa")
route.register(r'DetalhesUsuarios', apporionsviewsets.DetalhesUsuariosViewSet, basename="DetalhesUsuarios")
route.register(r'clientes', apporionsviewsets.ClientesViewSet, basename="clientes")
route.register(r'ItemCliente', apporionsviewsets.ItemClienteViewSet, basename="ItemCliente")
route.register(r'produto', apporionsviewsets.ProdutoViewSet, basename="Produto")
route.register(r'Servicos', apporionsviewsets.ServicosViewSet, basename="Servicos")
route.register(r'FormaPgto', apporionsviewsets.FormaPgtoViewSet, basename="FormaPgto")
route.register(r'Vendas', apporionsviewsets.VendasViewSet, basename="Vendas")
route.register(r'Operadora', apporionsviewsets.OperadoraViewSet, basename="Operadora")
route.register(r'users', apporionsviewsets.UserViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name='index'),
    path('empresa/', AutoCriarEmpresa.as_view(), name='empresa'),
    path('v1/',include(route.urls)),
    path('v1/auth/', include('rest_authtoken.urls')),
    path('v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('v1/api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('v1/detalhe/api-token-auth', CustomAuthToken.as_view())
]
