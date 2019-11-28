from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate
from django.urls import reverse_lazy

urlpatterns = [

    path('registrar/', UsuarioCreate.as_view(), name="user-create"),

    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),
    
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),

    path('alterar-senha/', auth_views.PasswordChangeView.as_view(
        template_name="usuarios/form.html",
        extra_context={
            'titulo': 'Alterar senha atual',
            'botao': 'Alterar',
            'classe': 'btn-success'
        },
        success_url=reverse_lazy('index')
    ), name="alterar-senha")

]
