from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from contact.forms import ContactForm
# from django.http import Http404
# Create your views here.

def create(request):
    if request.method == 'POST':
        context = {
        'title': 'Create',
        'form': ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context,
            )

    context = {
        'title': 'Create',
        'form': ContactForm()
    }
    return render(
        request,
        'contact/create.html',
        context,
    )