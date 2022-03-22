from django.contrib import admin
from django.urls import path, include
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.index, name='index'),
    path('books/', core.views.book_list, name='book_list'),
    path('books/<int:pk>/', core.views.book_detail, name='book_detail'),
]
