from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView

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
    success_url = reverse_lazy('listar-cliente')
    fields = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context = super(ClienteCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Estados"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ClienteExcluir(DeleteView):
    model = Cliente
    template_name="formulario.html"
    success_url = reverse_lazy("listar-cliente")
    fields = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(ClienteExcluir, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-cliente")
    fields = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(ClienteUpdate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Editar cadastro de Cliente"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ClienteListar(ListView):
    model = Cliente
    template_name = "listas/lista_cliente.html"
