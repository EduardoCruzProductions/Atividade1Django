from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from braces.views import GroupRequiredMixin

from .models import Cliente, Modulo, Produto, Venda, ItensVenda

# Create your views here.

class SobreView(TemplateView):
    template_name = "sobre.html"

class ContatoView(TemplateView):
    template_name = "contato.html"

class CurriculoView(TemplateView):
    template_name = "curriculo.html"


##################### CLIENTE ######################
class ClienteCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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

class ClienteExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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
    
class ClienteUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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

class ClienteListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Cliente
    template_name = "listas/lista_cliente.html"

##################### PRODUTO ######################
class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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

class ProdutoExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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

class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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

class ProdutoListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Produto
    template_name = "listas/lista_produto.html"

##################### MODULO ######################
class ModuloCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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

class ModuloExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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

class ModuloUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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

class ModuloListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Modulo
    template_name = "listas/lista_modulo.html"

##################### VENDA ######################
class VendaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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

class VendaExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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

class VendaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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

class VendaListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = Venda
    template_name = "listas/lista_venda.html"

##################### ITENS VENDA ######################
class ItensVendaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
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

class ItensVendaExcluir(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
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

class ItensVendaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
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

class ItensVendaListar(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    model = ItensVenda
    template_name = "listas/lista_itens_venda.html"