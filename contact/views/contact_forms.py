from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
# from django.http import Http404
# Create your views here.

def create(request):
    post = request.POST.get('first_name')
    context = {

    }
    return render(
        request,
        'contact/create.html',
        context,
    )