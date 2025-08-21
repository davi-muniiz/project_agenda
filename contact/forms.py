from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

class ContactForm(forms.ModelForm):


    first_name = forms.CharField(               # Altera e/ou coloca campos no HTML do forms (DJANGO).
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Escreva Aqui',
                
            }
        ),
        help_text="Texto de Ajuda"
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',           # Aceita imagem de todos os formatos.
            }
        )
    )


    
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture')  # Campos que aparecerão na hora de criar/update contato.

    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg1 = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            msg2 = ValidationError(
                'Segundo nome não pode ser igual ao primeiro',
                code='invalid'
            )
            self.add_error('first_name', msg1)
            self.add_error('last_name', msg2)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return first_name

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length= 3,
        
    )
    last_name = forms.CharField(
        required=True,
        min_length= 3,
        
    )
    email = forms.EmailField(
        required=True, 
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail!', code='invalid')
            )

        return email