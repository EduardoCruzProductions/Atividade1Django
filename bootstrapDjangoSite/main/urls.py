from django.urls import path

from main.views import IndexView
from main.views import SobreView

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
	path('sobre/', SobreView.as_view(), name="sobre"),
]
