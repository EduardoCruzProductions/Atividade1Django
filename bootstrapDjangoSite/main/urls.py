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

	# Modulo
	path('cadastro/modulo', ModuloCreate.as_view(), name="cadastro-modulo"),
	path('listar/modulo', ModuloListar.as_view(), name="listar-modulo"),
	path('excluir/modulo/<int:pk>', ModuloExcluir.as_view(), name="excluir-modulo"),
	path('alterar/modulo/<int:pk>', ModuloUpdate.as_view(), name="editar-modulo"),

	# Venda
	path('cadastro/venda', VendaCreate.as_view(), name="cadastro-venda"),
	path('listar/venda', VendaListar.as_view(), name="listar-venda"),
	path('excluir/venda/<int:pk>', VendaExcluir.as_view(), name="excluir-venda"),
	path('alterar/venda/<int:pk>', VendaUpdate.as_view(), name="editar-venda"),

	# Itens de Venda
	path('cadastro/itensvenda', ItensVendaCreate.as_view(), name="cadastro-itens-venda"),
	path('listar/itensvenda', ItensVendaListar.as_view(), name="listar-itens-venda"),
	path('excluir/itensvenda/<int:pk>', ItensVendaExcluir.as_view(), name="excluir-itens-venda"),
	path('alterar/itensvenda/<int:pk>', ItensVendaUpdate.as_view(), name="editar-itens-venda"),

]
