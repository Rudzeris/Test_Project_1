from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, ListView, DetailView

import core.models


class IndexView(TemplateView):
    template_name = 'core/index.html'


class Books(ListView):
    def get_queryset(self):
        name = self.request.GET.get('name')
        queryset = core.models.Book.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BookDetail(DetailView):
    queryset = core.models.Book.objects.all()

