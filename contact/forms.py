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


    
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data

        # self.add_error(
        #     'first_name', ValidationError(
        #         'Mensagem de Erro', code='invalid'
        #     )
        # )

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name is int or float:                  # Validação
            self.add_error(
                'first_name', ValidationError(
                    'Somente letras.', code='invalid'
                )
            )

        return first_name