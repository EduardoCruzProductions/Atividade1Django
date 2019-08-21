from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Cliente, Modulo, Produto, Venda, ItensVenda

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SobreView(TemplateView):
    template_name = "sobre.html"

class ContatoView(TemplateView):
    template_name = "contato.html"

class CurriculoView(TemplateView):
    template_name = "curriculo.html"


##################### CLIENTE ######################
class ClienteCreate(CreateView):
    model = Cliente
    template_name = "formulario.html"
    success_url = reverse_lazy('index')
    fields = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context = super(ClienteCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context

