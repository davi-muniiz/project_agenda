from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',  # Faz o Django Admin mostrar essas coisas que foram definidas no Contact
    ordering = 'id',                                            # Faz o Django Admin ordenar de acordo com o parâmetro colocado.
    # list_filter = 'created_date',                             # Cria uma 'tabela' para você selecionar filtros de pesquisa. Util ao ter muitos dados.
    search_fields = 'id', 'first_name', 'last_name',            # Define os campos de pesquisa permitidos.
    list_per_page = 50                                          # Máximo de dados por páginas.
    list_max_show_all = 200                                     # Máximo de dados se pressiona show_all.
    list_editable = 'first_name', 'last_name', 'show',          # Permite que os campos sejam editados com nula necessidade de adentrar ao contato para tal objetivo.
    list_display_links = 'id', 'phone',                         # Define o que será link nos campos de dados exibidos. ATENÇÃO: se o param. referido estiver em editable
                                                                # um erro ocorrerá.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',