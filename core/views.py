from django.shortcuts import render
import core.models

def index(request):
    books= core.models.Book.objects.all()
    return render(request, 'core/index.html', {'books':books})

def book_list(request, pk):
    books= core.models.Book.objects.all()
    return render(request, 'core/index.html', {'books':books})

def book_detail(request, pk):
    book= core.models.Book.objects.get(pk=pk)
    return render(request, 'core/index.html', {'book':book})

