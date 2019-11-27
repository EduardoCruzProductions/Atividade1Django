from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Cliente, Modulo, Produto, Venda, ItensVenda

# Create your views here.

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
        context['titulo'] = "Cadastro de novos Clientes"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class ClienteExcluir(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name="formulario.html"
    success_url = reverse_lazy("listar-cliente")
    fields = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context = super(ClienteExcluir, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context
    
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-cliente")
    fields = ['nome', 'cpf', 'email']
    def get_context_data(self, *args, **kwargs):
        context = super(ClienteUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Cliente"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
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
        context['titulo'] = "Cadastro de novos Produtos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class ProdutoExcluir(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name="formulario.html"
    success_url = reverse_lazy("listar-produto")
    fields = ['titulo', 'versao', 'dataLancamento', 'descricao']
    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoExcluir, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-cliente")
    fields = ['titulo', 'versao', 'dataLancamento', 'descricao']
    def get_context_data(self, *args, **kwargs):
        context = super(ProdutoUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Produto"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
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
        context['titulo'] = "Cadastro de novos Modulos"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class ModuloExcluir(LoginRequiredMixin, DeleteView):
    model = Modulo
    template_name="formulario.html"
    success_url = reverse_lazy("listar-modulo")
    fields = ['nome', 'versao', 'dataLancamento','preco', 'descricao', 'produto']
    def get_context_data(self, *args, **kwargs):
        context = super(ModuloExcluir, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class ModuloUpdate(LoginRequiredMixin, UpdateView):
    model = Modulo
    template_name = "formulario.html"
    success_url = reverse_lazy("listar-modulo")
    fields = ['nome', 'versao', 'dataLancamento','preco', 'descricao', 'produto']
    def get_context_data(self, *args, **kwargs):
        context = super(ModuloUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Modulo"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context

class ModuloListar(LoginRequiredMixin, ListView):
    model = Modulo
    template_name = "listas/lista_modulo.html"

##################### VENDA ######################
class VendaCreate(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-venda')
    fields = ['cliente', 'total', 'desconto']
    def get_context_data(self, *args, **kwargs):
        context = super(VendaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novas Vendas"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class VendaExcluir(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name="formulario.html"
    success_url = reverse_lazy('listar-venda')
    fields = ['cliente', 'total', 'desconto']
    def get_context_data(self, *args, **kwargs):
        context = super(VendaExcluir, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class VendaUpdate(LoginRequiredMixin, UpdateView):
    model = Venda
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-venda')
    fields = ['cliente', 'total', 'desconto']
    def get_context_data(self, *args, **kwargs):
        context = super(VendaUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Venda"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context

class VendaListar(LoginRequiredMixin, ListView):
    model = Venda
    template_name = "listas/lista_venda.html"

##################### ITENS VENDA ######################
class ItensVendaCreate(LoginRequiredMixin, CreateView):
    model = ItensVenda
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-itens-venda')
    fields = ['modulo', 'venda', 'total', 'desconto']
    def get_context_data(self, *args, **kwargs):
        context = super(ItensVendaCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Itens de Venda"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-primary"
        return context

class ItensVendaExcluir(LoginRequiredMixin, DeleteView):
    model = ItensVenda
    template_name="formulario.html"
    success_url = reverse_lazy('listar-itens-venda')
    fields = ['modulo', 'venda', 'total', 'desconto']
    def get_context_data(self, *args, **kwargs):
        context = super(ItensVendaExcluir, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Deseja excluir esse registro?"
        context['botao'] = "Excluir"
        context['classeBotao'] = "btn-danger"
        return context

class ItensVendaUpdate(LoginRequiredMixin, UpdateView):
    model = ItensVenda
    template_name = "formulario.html"
    success_url = reverse_lazy('listar-itens-venda')
    fields = ['modulo', 'venda', 'total', 'desconto']
    def get_context_data(self, *args, **kwargs):
        context = super(ItensVendaUpdate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Item de Venda"
        context['botao'] = "Salvar"
        context['classeBotao'] = "btn-success"
        return context

class ItensVendaListar(LoginRequiredMixin, ListView):
    model = ItensVenda
    template_name = "listas/lista_itens_venda.html"