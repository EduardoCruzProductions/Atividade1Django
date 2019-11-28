from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import News
from django.shortcuts import get_object_or_404
from braces.views import GroupRequiredMixin

# Create your views here.
class IndexView(ListView):
    model = News
    template_name = "index.html"

class NewsCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    model = News
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-noticia')
    fields = ['titulo', 'resumo', 'conteudo']

    def get_context_data(self, *args, **kwargs):
        context = super(NewsCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Nova noticia"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class NewsExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    model = News
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-noticia')
    fields = ['titulo', 'resumo', 'conteudo']
    
    def get_context_data(self, *args, **kwargs):
        context = super(NewsExcluir, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(News, pk=self.kwargs['pk'],
        usuario = self.request.user)
        return self.object

class NewsUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    model = News
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-noticia')
    fields = ['titulo', 'resumo', 'conteudo']
    def get_context_data(self, *args, **kwargs):
        context = super(NewsUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar noticia"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context

    def get_object(self, queryset=None):
        self.object = get_object_or_404(News, pk=self.kwargs['pk'],
        usuario=self.request.user)
        return self.object

class NewsListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = News
    template_name = "lista_noticia.html"
    def get_queryset(self):
        self.object_list = News.objects.filter(usuario=self.request.user)
        return self.object_list