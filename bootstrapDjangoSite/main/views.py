from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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
class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-cliente')
    fields = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context = super(ClienteCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Clientes"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ClienteExcluir(LoginRequiredMixin, DeleteView):
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

class ClienteUpdate(LoginRequiredMixin, UpdateView):
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

class ClienteListar(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "listas/lista_cliente.html"


##################### PRODUTO ######################
class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-produto')
    fields = ['titulo', 'versao', 'dataLancamento', 'descricao']
    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Produtos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ProdutoExcluir(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name="formulario.html"
    success_url = reverse_lazy("listar-produto")
    fields = ['titulo', 'versao', 'dataLancamento', 'descricao']
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(ProdutoExcluir, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-cliente")
    fields = ['titulo', 'versao', 'dataLancamento', 'descricao']
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(ProdutoUpdate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Editar cadastro de Produto"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ProdutoListar(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "listas/lista_produto.html"

##################### MODULO ######################
class ModuloCreate(LoginRequiredMixin, CreateView):
    model = Modulo
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-modulo')
    fields = ['nome', 'versao', 'dataLancamento','preco', 'descricao', 'produto']
    def get_context_data(self, *args, **kwargs):
        context = super(ModuloCreate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Cadastro de novos Modulos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ModuloExcluir(LoginRequiredMixin, DeleteView):
    model = Modulo
    template_name="formulario.html"
    success_url = reverse_lazy("listar-modulo")
    fields = ['nome', 'versao', 'dataLancamento','preco', 'descricao', 'produto']
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(ModuloExcluir, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ModuloUpdate(LoginRequiredMixin, UpdateView):
    model = Modulo
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-modulo")
    fields = ['nome', 'versao', 'dataLancamento','preco', 'descricao', 'produto']
    def get_context_data(self, *args, **kwargs):
        # Chamar o "pai" para que sempre tenha o comportamento padrão, além do nosso
        context = super(ModuloUpdate, self).get_context_data(*args, **kwargs)

        # Adicionar coisas ao contexto que serão enviadas para o html
        context['titulo'] = "Editar cadastro de Modulo"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"

        # Devolve/envia o context para seu comportamento padrão
        return context

class ModuloListar(LoginRequiredMixin, ListView):
    model = Modulo
    template_name = "listas/lista_modulo.html"