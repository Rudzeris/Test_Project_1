from django.db import models


class Author(models.Model):
    name = models.CharField('Имя', max_length=128)


class AuthorProfile(models.Model):
    author = models.OneToOneField


class Book(models.Model):
    author = models.ForeignKey('core.Author', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField('Название', max_length=128)
    pages = models.IntegerField('Количество страниц', blank=True, null=True)

    class Meta:
        ordering=['pages']
        verbose_name='Книги'
        verbose_name_plural='Книги'

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateField()
    book = models.ManyToManyField('core.Book')