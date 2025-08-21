from django import forms
from django.core.exceptions import ValidationError

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