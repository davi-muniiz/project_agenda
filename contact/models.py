from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'      # Corrige o "erro" que faz mostrar 'categorys' no Django Admin.

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name                        # No painel do Django Admin, o __str__ é responsável por mostrar o name que você definir em vez de algo tipo "exemplo.Exemplo".

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category,                   # Recebe a Caregory por foreign_key, o que ajuda na configuração e a não dar erros, além de organizar e otimizar o código.
        on_delete=models.SET_NULL,  # Configura o comportamento se excluido a Category.
        null=True, blank=True       # Se null, é obrigatório setar null = True para não dar erro, e Blank=True se quiser deixar opcional.
        )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' # No painel do Django Admin, o __str__ é responsável por mostrar o name que você definir em vez de algo tipo "exemplo.Exemplo".
    
