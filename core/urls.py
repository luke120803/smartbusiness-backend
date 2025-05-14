# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    EmpresaViewSet, CategoriaViewSet, ReceitaViewSet,
    DespesaViewSet, ProdutoViewSet, VendaViewSet
)

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'despesas', DespesaViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
