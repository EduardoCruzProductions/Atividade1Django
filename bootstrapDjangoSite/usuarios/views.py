from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404

class UsuarioCreate(CreateView):
    form_class = UserCreationForm
    template_name = "usuarios/formulario.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *args, **kwargs):
        context = super(UsuarioCreate, self).get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de novos Usuários"
        context['botao'] = "Cadastrar"
        context['classeBotao'] = "btn-success"
        return context

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Usuário")

        url = super().form_valid(form)

        if grupo:
            self.object.groups.add(grupo)
            self.object.save()

        return url
