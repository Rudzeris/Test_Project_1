from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
import core.models

def index(request):
    books= core.models.Book.objects.all()
    return render(request, 'core/index.html', {'books':books})

def book_list(request):
    books= core.models.Book.objects.all()
    return render(request, 'core/book_list.html', {'books':books})

def book_detail(request, pk):

    book = get_object_or_404(core.models.Book,pk=pk)
    return render(request, 'core/book_detail.html', {'book':book})

