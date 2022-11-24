from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #Formulário por padrão do Django
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm): #Formulário padrão para registro de Usuários
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2'] #Verificação de Senha

    def clean_email(self): #Verificação de E-mail
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O e-mail {} já está em uso.".format(e))
        return e