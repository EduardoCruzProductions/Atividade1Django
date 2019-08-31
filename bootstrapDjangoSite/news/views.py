from django.shortcuts import render
from django.views.generic.list import ListView
from .models import News

# Create your views here.
class IndexView(ListView):
    model = News
    template_name = "index.html"