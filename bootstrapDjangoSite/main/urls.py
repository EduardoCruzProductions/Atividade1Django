from django.urls import path

from main.views import *

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('sobre/', SobreView.as_view(), name="sobre"),
	path('contato/', ContatoView.as_view(), name="contato"),
	path('curriculum/', CurriculoView.as_view(), name="curriculum"),
]
