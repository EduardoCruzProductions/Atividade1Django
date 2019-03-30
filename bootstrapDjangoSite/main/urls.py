from django.urls import path

from main.views import IndexView
from main.views import SobreView
from main.views import ContatoView

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('sobre/', SobreView.as_view(), name="sobre"),
	path('contato/', ContatoView.as_view(), name="contato"),
]
