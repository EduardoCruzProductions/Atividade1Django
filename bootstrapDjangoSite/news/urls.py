from django.urls import path

from news.views import *

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('cadastro/noticia', NewsCreate.as_view(), name="cadastro-noticia"),
	path('alterar/noticia/<int:pk>', NewsUpdate.as_view(), name="editar-noticia"),
	path('excluir/noticia/<int:pk>', NewsExcluir.as_view(), name="excluir-noticia"),
	path('listar/noticia', NewsListar.as_view(), name="listar-noticia"),
	path('noticia/<int:pk>', NewsDetalhes.as_view(), name="noticia"),
]