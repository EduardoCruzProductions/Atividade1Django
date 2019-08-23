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

]
