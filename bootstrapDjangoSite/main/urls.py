from django.urls import path

from main.views import *

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('sobre/', SobreView.as_view(), name="sobre"),
	path('contato/', ContatoView.as_view(), name="contato"),
	path('curriculum/', CurriculoView.as_view(), name="curriculum"),

	# Cliente
	path('cadastro/cliente', ClienteCreate.as_view(), name="cadastro-cliente"),
	path('listar/cliente', ClienteListar.as_view(), name="listar-cliente"),
	path('excluir/cliente/<int:pk>/', ClienteExcluir.as_view(), name="excluir-cliente"),
	path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name="editar-cliente"),

	# Produto
	path('cadastro/produto', ProdutoCreate.as_view(), name="cadastro-produto"),
	path('listar/produto', ProdutoListar.as_view(), name="listar-produto"),
	path('excluir/produto/<int:pk>', ProdutoExcluir.as_view(), name="excluir-produto"),
	path('alterar/produto/<int:pk>', ProdutoUpdate.as_view(), name="editar-produto"),


]
