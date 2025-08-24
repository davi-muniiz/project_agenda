from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def register(request):
    form = RegisterForm()

    

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)                       # Utiliza o sistema de login do Django para logar o user.
            messages.success(request, 'Logado com Sucesso')
            return redirect('contact:index')      
        messages.error(request, 'Login Inválido!')

    return render(
        request,
        'contact/login.html',
        {
            'title': 'Login',
            'form': form,
        }
    )

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'title': 'Update',
                'form': form,
            }
        )
    
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {
                'title': 'Update',
                'form': form,
            }
        )
    form.save()

    return redirect('contact:user_update')
   


def logout_view(request):
    auth.logout(request)   # Utiliza o sistema de logout do Django para deslogar o user.
    return redirect(
        'contact:login'
    )