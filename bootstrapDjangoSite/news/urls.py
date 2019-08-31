from django.urls import path

from news.views import *

urlpatterns = [
	path('', IndexView.as_view(), name="index"),
]